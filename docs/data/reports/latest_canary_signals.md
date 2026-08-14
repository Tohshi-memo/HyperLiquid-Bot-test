# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:46:28.438981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0341` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0075` n `114`; fx avg `0.0063` n `6`; index avg `-0.0018` n `25`; metal avg `0.0152` n `20`; unknown avg `0.1064` n `791`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0151` n `230`; crypto_major avg `0.0254` n `8`; equity avg `-0.0042` n `114`; fx avg `-0.0133` n `6`; index avg `0.0112` n `25`; metal avg `0.0413` n `20`; unknown avg `0.1454` n `791`
- 4h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.1741` n `230`; crypto_major avg `-0.1769` n `8`; equity avg `0.1602` n `114`; fx avg `0.0213` n `6`; index avg `0.0519` n `25`; metal avg `0.0422` n `20`; unknown avg `8.5465` n `791`
- 24h: commodity avg `0.1713` n `12`; crypto_alt avg `0.0617` n `230`; crypto_major avg `-0.9767` n `8`; equity avg `-0.5305` n `114`; fx avg `0.0754` n `6`; index avg `-0.0671` n `25`; metal avg `0.245` n `20`; unknown avg `-0.1031` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
