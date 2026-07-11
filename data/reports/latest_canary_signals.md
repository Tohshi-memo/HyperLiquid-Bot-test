# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T04:07:30.096099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.07` n `229`; crypto_major avg `-0.1034` n `8`; equity avg `-0.0213` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.2177` n `765`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.1067` n `229`; crypto_major avg `-0.0169` n `8`; equity avg `-0.0466` n `92`; fx avg `-0.0003` n `6`; index avg `0.0024` n `25`; metal avg `0.0116` n `20`; unknown avg `-0.0856` n `763`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.152` n `229`; crypto_major avg `-0.1376` n `8`; equity avg `-0.0089` n `92`; fx avg `-0.002` n `6`; index avg `0.0015` n `25`; metal avg `0.0096` n `20`; unknown avg `3.2195` n `763`
- 24h: commodity avg `-0.3631` n `12`; crypto_alt avg `0.3865` n `229`; crypto_major avg `-0.3414` n `8`; equity avg `-0.8617` n `92`; fx avg `-0.1613` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0444` n `20`; unknown avg `3.3547` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
