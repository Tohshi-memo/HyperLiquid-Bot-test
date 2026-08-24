# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T11:37:23.443094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `0.8194` n `231`; crypto_major avg `0.8818` n `8`; equity avg `0.3784` n `122`; fx avg `-0.004` n `6`; index avg `0.0768` n `25`; metal avg `0.1518` n `20`; unknown avg `0.1278` n `793`
- 1h: commodity avg `0.1413` n `12`; crypto_alt avg `0.6275` n `227`; crypto_major avg `0.7468` n `8`; equity avg `0.0722` n `106`; fx avg `0.019` n `6`; index avg `0.0265` n `25`; metal avg `0.118` n `20`; unknown avg `0.1347` n `785`
- 4h: commodity avg `0.18` n `12`; crypto_alt avg `1.0249` n `231`; crypto_major avg `0.9977` n `8`; equity avg `0.1294` n `122`; fx avg `-0.0216` n `6`; index avg `0.0347` n `25`; metal avg `0.0725` n `20`; unknown avg `0.5487` n `793`
- 24h: commodity avg `-0.0684` n `12`; crypto_alt avg `1.5606` n `231`; crypto_major avg `0.6233` n `8`; equity avg `-1.2773` n `122`; fx avg `-0.1168` n `6`; index avg `-0.0951` n `25`; metal avg `0.2726` n `20`; unknown avg `5.1653` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
