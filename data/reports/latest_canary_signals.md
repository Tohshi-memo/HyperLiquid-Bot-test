# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:52:25.177824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `0.0768` n `8`; equity avg `0.0039` n `114`; fx avg `0.0021` n `6`; index avg `0.003` n `25`; metal avg `0.0478` n `20`; unknown avg `0.1279` n `791`
- 1h: commodity avg `-0.1311` n `12`; crypto_alt avg `-0.031` n `230`; crypto_major avg `-0.1801` n `8`; equity avg `-0.0101` n `114`; fx avg `-0.0115` n `6`; index avg `0.0133` n `25`; metal avg `0.0834` n `20`; unknown avg `-0.0027` n `791`
- 4h: commodity avg `-0.1422` n `12`; crypto_alt avg `-0.8437` n `230`; crypto_major avg `-0.6483` n `8`; equity avg `0.0008` n `114`; fx avg `-0.0113` n `6`; index avg `0.0292` n `25`; metal avg `0.0381` n `20`; unknown avg `0.0922` n `791`
- 24h: commodity avg `-0.0498` n `12`; crypto_alt avg `-1.0113` n `230`; crypto_major avg `-0.6574` n `8`; equity avg `0.277` n `114`; fx avg `-0.0179` n `6`; index avg `0.0612` n `25`; metal avg `0.0953` n `20`; unknown avg `0.0387` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
