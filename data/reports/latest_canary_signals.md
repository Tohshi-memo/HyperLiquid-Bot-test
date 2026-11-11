# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T15:37:28.056938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `13`; crypto_alt avg `0.9142` n `239`; crypto_major avg `1.1141` n `8`; equity avg `0.5883` n `161`; fx avg `0.006` n `6`; index avg `0.0494` n `27`; metal avg `0.007` n `20`; unknown avg `0.341` n `1261`
- 1h: commodity avg `0.3307` n `13`; crypto_alt avg `0.8084` n `239`; crypto_major avg `1.0621` n `8`; equity avg `1.3131` n `161`; fx avg `0.0326` n `6`; index avg `0.1128` n `27`; metal avg `-0.0019` n `20`; unknown avg `-0.1499` n `1255`
- 4h: commodity avg `0.5226` n `13`; crypto_alt avg `1.1465` n `239`; crypto_major avg `1.0368` n `8`; equity avg `0.851` n `161`; fx avg `0.0079` n `6`; index avg `0.0414` n `27`; metal avg `-0.2883` n `20`; unknown avg `19.0654` n `1231`
- 24h: commodity avg `1.4631` n `13`; crypto_alt avg `1.0333` n `239`; crypto_major avg `1.6201` n `8`; equity avg `4.2786` n `161`; fx avg `-0.1507` n `6`; index avg `0.3532` n `27`; metal avg `0.1726` n `20`; unknown avg `2.1422` n `1155`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.3514`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
