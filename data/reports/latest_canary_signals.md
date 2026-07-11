# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T12:22:25.825618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `-0.0291` n `230`; crypto_major avg `-0.0318` n `8`; equity avg `-0.0139` n `92`; fx avg `-0.003` n `6`; index avg `-0.0006` n `25`; metal avg `-0.003` n `20`; unknown avg `0.003` n `765`
- 1h: commodity avg `0.0618` n `12`; crypto_alt avg `0.1757` n `230`; crypto_major avg `0.0606` n `8`; equity avg `-0.0198` n `92`; fx avg `-0.0106` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.0213` n `765`
- 4h: commodity avg `0.0586` n `12`; crypto_alt avg `0.2384` n `230`; crypto_major avg `0.147` n `8`; equity avg `-0.0071` n `92`; fx avg `-0.0092` n `6`; index avg `0.0001` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.2028` n `761`
- 24h: commodity avg `-0.1155` n `12`; crypto_alt avg `0.2161` n `229`; crypto_major avg `-0.4806` n `8`; equity avg `-0.3204` n `92`; fx avg `-0.0983` n `6`; index avg `0.1168` n `25`; metal avg `0.1272` n `20`; unknown avg `2.8125` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
