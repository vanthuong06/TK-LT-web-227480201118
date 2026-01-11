"""
HTMLTestRunner - A simple HTML test runner for unittest
"""
import sys
import io
import time
from unittest import TestResult


class HTMLTestResult(TestResult):
    """Test result class that outputs HTML"""
    
    def __init__(self, stream, descriptions, verbosity):
        super(HTMLTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.startTime = None
        self.stopTime = None
        self.testCases = []
    
    def startTest(self, test):
        super(HTMLTestResult, self).startTest(test)
        self.testCases.append({
            'name': self.getDescription(test),
            'status': 'running',
            'output': '',
            'error': '',
            'time': 0
        })
    
    def addSuccess(self, test):
        super(HTMLTestResult, self).addSuccess(test)
        if self.testCases:
            self.testCases[-1]['status'] = 'success'
    
    def addError(self, test, err):
        super(HTMLTestResult, self).addError(test, err)
        if self.testCases:
            self.testCases[-1]['status'] = 'error'
            self.testCases[-1]['error'] = self._exc_info_to_string(err, test)
    
    def addFailure(self, test, err):
        super(HTMLTestResult, self).addFailure(test, err)
        if self.testCases:
            self.testCases[-1]['status'] = 'failure'
            self.testCases[-1]['error'] = self._exc_info_to_string(err, test)
    
    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return doc_first_line
        else:
            return str(test)


class HTMLTestRunner:
    """A test runner that outputs HTML"""
    
    def __init__(self, stream=None, title=None, description=None, verbosity=1):
        if stream is None:
            stream = sys.stdout
        self.stream = stream
        self.title = title or "Test Results"
        self.description = description or ""
        self.verbosity = verbosity
    
    def run(self, test):
        """Run the given test case or test suite"""
        result = HTMLTestResult(self.stream, self.descriptions, self.verbosity)
        result.startTime = time.time()
        
        test(result)
        
        result.stopTime = time.time()
        self.generateReport(result)
        return result
    
    @property
    def descriptions(self):
        return self.verbosity > 1
    
    def generateReport(self, result):
        """Generate HTML report"""
        duration = result.stopTime - result.startTime
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .summary {{
            background-color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .summary td {{
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }}
        .summary td:first-child {{
            font-weight: bold;
            width: 200px;
        }}
        .test-case {{
            background-color: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
            border-left: 4px solid #ddd;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .test-case.success {{
            border-left-color: #4CAF50;
        }}
        .test-case.failure {{
            border-left-color: #f44336;
        }}
        .test-case.error {{
            border-left-color: #ff9800;
        }}
        .test-name {{
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 5px;
        }}
        .test-status {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 3px;
            font-size: 12px;
            margin-left: 10px;
        }}
        .status-success {{
            background-color: #4CAF50;
            color: white;
        }}
        .status-failure {{
            background-color: #f44336;
            color: white;
        }}
        .status-error {{
            background-color: #ff9800;
            color: white;
        }}
        .error-details {{
            background-color: #f5f5f5;
            padding: 10px;
            margin-top: 10px;
            border-radius: 3px;
            font-family: monospace;
            font-size: 12px;
            white-space: pre-wrap;
        }}
        .stats {{
            display: flex;
            gap: 20px;
            margin-top: 10px;
        }}
        .stat-box {{
            flex: 1;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 3px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 24px;
            font-weight: bold;
        }}
        .stat-label {{
            font-size: 12px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{self.title}</h1>
        <p>{self.description}</p>
    </div>
    
    <div class="summary">
        <h2>Tổng quan</h2>
        <table>
            <tr>
                <td>Tổng số test cases:</td>
                <td>{result.testsRun}</td>
            </tr>
            <tr>
                <td>Thành công:</td>
                <td style="color: #4CAF50; font-weight: bold;">{result.testsRun - len(result.failures) - len(result.errors)}</td>
            </tr>
            <tr>
                <td>Thất bại:</td>
                <td style="color: #f44336; font-weight: bold;">{len(result.failures)}</td>
            </tr>
            <tr>
                <td>Lỗi:</td>
                <td style="color: #ff9800; font-weight: bold;">{len(result.errors)}</td>
            </tr>
            <tr>
                <td>Thời gian thực thi:</td>
                <td>{duration:.2f} giây</td>
            </tr>
        </table>
        
        <div class="stats">
            <div class="stat-box">
                <div class="stat-number" style="color: #4CAF50;">{result.testsRun - len(result.failures) - len(result.errors)}</div>
                <div class="stat-label">Thành công</div>
            </div>
            <div class="stat-box">
                <div class="stat-number" style="color: #f44336;">{len(result.failures)}</div>
                <div class="stat-label">Thất bại</div>
            </div>
            <div class="stat-box">
                <div class="stat-number" style="color: #ff9800;">{len(result.errors)}</div>
                <div class="stat-label">Lỗi</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">{duration:.2f}s</div>
                <div class="stat-label">Thời gian</div>
            </div>
        </div>
    </div>
    
    <h2>Chi tiết Test Cases</h2>
"""
        
        for test_case in result.testCases:
            status_class = test_case['status']
            status_text = {
                'success': 'Thành công',
                'failure': 'Thất bại',
                'error': 'Lỗi'
            }.get(status_class, 'Chưa xác định')
            
            status_badge = f'<span class="test-status status-{status_class}">{status_text}</span>'
            
            error_html = ''
            if test_case['error']:
                error_html = f'<div class="error-details">{self._escape_html(test_case["error"])}</div>'
            
            html += f"""
    <div class="test-case {status_class}">
        <div class="test-name">
            {self._escape_html(test_case['name'])} {status_badge}
        </div>
        {error_html}
    </div>
"""
        
        html += """
</body>
</html>
"""
        
        self.stream.write(html)
    
    def _escape_html(self, text):
        """Escape HTML special characters"""
        if not text:
            return ''
        return (str(text)
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#x27;'))

