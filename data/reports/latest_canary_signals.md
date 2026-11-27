# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T21:52:26.413326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.027` n `239`; crypto_major avg `-0.1106` n `8`; equity avg `-0.0219` n `168`; fx avg `-0.0` n `6`; index avg `-0.0087` n `27`; metal avg `0.0006` n `20`; unknown avg `5.8118` n `1257`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `0.1165` n `239`; crypto_major avg `-0.0668` n `8`; equity avg `-0.0204` n `168`; fx avg `0.008` n `6`; index avg `-0.0213` n `27`; metal avg `0.0066` n `20`; unknown avg `2.0292` n `1181`
- 4h: commodity avg `0.0868` n `13`; crypto_alt avg `0.5547` n `239`; crypto_major avg `0.4607` n `8`; equity avg `0.7069` n `168`; fx avg `-0.0018` n `6`; index avg `0.0916` n `27`; metal avg `0.2696` n `20`; unknown avg `181.6155` n `1160`
- 24h: commodity avg `-0.4798` n `13`; crypto_alt avg `-0.0633` n `239`; crypto_major avg `-0.3295` n `8`; equity avg `3.0193` n `168`; fx avg `-0.1464` n `6`; index avg `0.3228` n `27`; metal avg `0.93` n `20`; unknown avg `279.0954` n `997`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
