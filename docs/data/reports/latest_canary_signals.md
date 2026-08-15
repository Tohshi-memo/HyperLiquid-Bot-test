# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T06:07:28.675702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0013` n `230`; crypto_major avg `0.0129` n `8`; equity avg `-0.0055` n `114`; fx avg `0.0084` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0262` n `765`
- 1h: commodity avg `0.0253` n `12`; crypto_alt avg `-0.0048` n `230`; crypto_major avg `-0.1437` n `8`; equity avg `-0.0738` n `114`; fx avg `0.0151` n `6`; index avg `-0.0162` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.1123` n `759`
- 4h: commodity avg `0.055` n `12`; crypto_alt avg `0.2737` n `230`; crypto_major avg `0.0049` n `8`; equity avg `-0.0272` n `114`; fx avg `0.0685` n `6`; index avg `-0.0261` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.0225` n `759`
- 24h: commodity avg `0.044` n `12`; crypto_alt avg `0.6742` n `230`; crypto_major avg `-0.2461` n `8`; equity avg `-0.0544` n `114`; fx avg `0.1831` n `6`; index avg `-0.0809` n `25`; metal avg `0.3033` n `20`; unknown avg `-0.116` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
