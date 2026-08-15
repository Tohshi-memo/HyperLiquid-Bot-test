# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:34:05.794065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.0868` n `230`; crypto_major avg `0.084` n `8`; equity avg `-0.0024` n `114`; fx avg `0.0006` n `6`; index avg `0.0019` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0075` n `791`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `0.2728` n `230`; crypto_major avg `0.1506` n `8`; equity avg `0.0231` n `114`; fx avg `0.0025` n `6`; index avg `0.0086` n `25`; metal avg `-0.0059` n `20`; unknown avg `5.122` n `791`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `0.3737` n `230`; crypto_major avg `0.2456` n `8`; equity avg `0.075` n `114`; fx avg `-0.0026` n `6`; index avg `0.0215` n `25`; metal avg `-0.02` n `20`; unknown avg `-0.0526` n `791`
- 24h: commodity avg `-0.1168` n `12`; crypto_alt avg `1.3571` n `230`; crypto_major avg `0.264` n `8`; equity avg `0.365` n `114`; fx avg `0.0328` n `6`; index avg `0.042` n `25`; metal avg `0.0219` n `20`; unknown avg `-0.0157` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
