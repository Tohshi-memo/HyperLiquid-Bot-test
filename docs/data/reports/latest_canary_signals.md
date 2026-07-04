# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T00:22:34.591749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.94` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.2466` n `229`; crypto_major avg `-0.1143` n `8`; equity avg `0.0254` n `88`; fx avg `0.0157` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.6044` n `765`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `0.0193` n `229`; crypto_major avg `0.1398` n `8`; equity avg `-0.0124` n `88`; fx avg `0.0031` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.418` n `765`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0207` n `229`; crypto_major avg `0.1214` n `8`; equity avg `0.0856` n `88`; fx avg `-0.0078` n `6`; index avg `-0.0357` n `25`; metal avg `0.0233` n `20`; unknown avg `1.3095` n `765`
- 24h: commodity avg `0.1742` n `12`; crypto_alt avg `3.0722` n `229`; crypto_major avg `3.308` n `8`; equity avg `1.7129` n `88`; fx avg `-0.1641` n `6`; index avg `0.4239` n `25`; metal avg `0.384` n `20`; unknown avg `5.5099` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
