# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:54:53.729977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `0.0683` n `230`; crypto_major avg `0.0868` n `8`; equity avg `0.0068` n `114`; fx avg `0.0056` n `6`; index avg `0.0026` n `25`; metal avg `0.0593` n `20`; unknown avg `0.122` n `791`
- 1h: commodity avg `-0.1383` n `12`; crypto_alt avg `-0.0275` n `230`; crypto_major avg `-0.1702` n `8`; equity avg `-0.0072` n `114`; fx avg `-0.008` n `6`; index avg `0.0129` n `25`; metal avg `0.0948` n `20`; unknown avg `-0.0123` n `791`
- 4h: commodity avg `-0.1495` n `12`; crypto_alt avg `-0.8406` n `230`; crypto_major avg `-0.6384` n `8`; equity avg `0.0037` n `114`; fx avg `-0.0078` n `6`; index avg `0.0288` n `25`; metal avg `0.0496` n `20`; unknown avg `0.0786` n `791`
- 24h: commodity avg `-0.0571` n `12`; crypto_alt avg `-1.0079` n `230`; crypto_major avg `-0.6475` n `8`; equity avg `0.2798` n `114`; fx avg `-0.0144` n `6`; index avg `0.0608` n `25`; metal avg `0.1068` n `20`; unknown avg `0.0396` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
