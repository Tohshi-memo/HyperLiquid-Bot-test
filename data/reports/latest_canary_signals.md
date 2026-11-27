# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T14:37:26.592225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2667` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1161` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `-0.7717` n `239`; crypto_major avg `-1.1157` n `8`; equity avg `-1.4221` n `168`; fx avg `0.0035` n `6`; index avg `-0.1075` n `27`; metal avg `-0.0523` n `20`; unknown avg `6.205` n `1264`
- 1h: commodity avg `0.0097` n `13`; crypto_alt avg `-0.945` n `239`; crypto_major avg `-1.2636` n `8`; equity avg `-1.5751` n `168`; fx avg `0.0008` n `6`; index avg `-0.1475` n `27`; metal avg `-0.0737` n `20`; unknown avg `1.8643` n `1260`
- 4h: commodity avg `-0.378` n `13`; crypto_alt avg `-0.84` n `239`; crypto_major avg `-1.4302` n `8`; equity avg `-2.0331` n `168`; fx avg `-0.0201` n `6`; index avg `-0.1635` n `27`; metal avg `-0.4703` n `20`; unknown avg `21.8925` n `1251`
- 24h: commodity avg `-0.2494` n `13`; crypto_alt avg `0.9074` n `239`; crypto_major avg `1.2255` n `8`; equity avg `1.737` n `168`; fx avg `-0.1118` n `6`; index avg `0.1414` n `27`; metal avg `0.6987` n `20`; unknown avg `88.0757` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
