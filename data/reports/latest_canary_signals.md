# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T15:07:30.993176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.0953` n `230`; crypto_major avg `0.0647` n `8`; equity avg `-0.2168` n `114`; fx avg `0.0072` n `6`; index avg `-0.0237` n `25`; metal avg `0.0228` n `20`; unknown avg `-0.0105` n `791`
- 1h: commodity avg `0.0937` n `12`; crypto_alt avg `-0.13` n `230`; crypto_major avg `0.0129` n `8`; equity avg `-0.7128` n `114`; fx avg `0.0125` n `6`; index avg `-0.1219` n `25`; metal avg `-0.0396` n `20`; unknown avg `-0.0196` n `786`
- 4h: commodity avg `0.1538` n `12`; crypto_alt avg `-0.0584` n `230`; crypto_major avg `-0.2127` n `8`; equity avg `-0.6523` n `114`; fx avg `0.0557` n `6`; index avg `-0.11` n `25`; metal avg `0.2479` n `20`; unknown avg `-0.4066` n `786`
- 24h: commodity avg `0.0693` n `12`; crypto_alt avg `-1.1631` n `230`; crypto_major avg `-1.3861` n `8`; equity avg `-0.4512` n `114`; fx avg `0.0296` n `6`; index avg `-0.0558` n `25`; metal avg `0.1581` n `20`; unknown avg `0.243` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
