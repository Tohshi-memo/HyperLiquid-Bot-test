# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T21:22:29.773767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `13`; crypto_alt avg `0.3944` n `237`; crypto_major avg `0.3266` n `8`; equity avg `0.1128` n `151`; fx avg `-0.0049` n `6`; index avg `0.0067` n `26`; metal avg `0.0161` n `20`; unknown avg `0.1135` n `1188`
- 1h: commodity avg `0.0077` n `13`; crypto_alt avg `0.3572` n `237`; crypto_major avg `0.4992` n `8`; equity avg `0.0724` n `151`; fx avg `-0.0087` n `6`; index avg `0.0084` n `26`; metal avg `0.0219` n `20`; unknown avg `1.5796` n `1180`
- 4h: commodity avg `0.0349` n `13`; crypto_alt avg `-1.4169` n `237`; crypto_major avg `-0.4394` n `8`; equity avg `-0.1529` n `151`; fx avg `-0.0531` n `6`; index avg `-0.0366` n `26`; metal avg `-0.029` n `20`; unknown avg `3.4805` n `1146`
- 24h: commodity avg `0.0605` n `13`; crypto_alt avg `-4.5678` n `236`; crypto_major avg `-1.8743` n `8`; equity avg `-0.8872` n `151`; fx avg `-0.051` n `6`; index avg `-0.1366` n `26`; metal avg `-0.0773` n `20`; unknown avg `1.4305` n `1001`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2097`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1418`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0761`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
