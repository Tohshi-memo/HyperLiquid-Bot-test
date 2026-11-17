# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T20:37:23.344218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0608` n `13`; crypto_alt avg `0.4394` n `239`; crypto_major avg `0.2759` n `8`; equity avg `0.1616` n `163`; fx avg `0.0043` n `6`; index avg `0.0346` n `27`; metal avg `0.0309` n `20`; unknown avg `1.59` n `1265`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `0.9134` n `239`; crypto_major avg `0.7485` n `8`; equity avg `0.2562` n `163`; fx avg `-0.0102` n `6`; index avg `0.0256` n `27`; metal avg `-0.0165` n `20`; unknown avg `3.229` n `1255`
- 4h: commodity avg `-0.0412` n `13`; crypto_alt avg `0.7183` n `239`; crypto_major avg `1.0593` n `8`; equity avg `0.6996` n `163`; fx avg `0.007` n `6`; index avg `0.0664` n `27`; metal avg `-0.0905` n `20`; unknown avg `2.1388` n `1253`
- 24h: commodity avg `0.1508` n `13`; crypto_alt avg `0.2792` n `239`; crypto_major avg `0.3939` n `8`; equity avg `-1.1506` n `163`; fx avg `0.0298` n `6`; index avg `-0.1276` n `27`; metal avg `-0.0287` n `20`; unknown avg `6.2477` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
