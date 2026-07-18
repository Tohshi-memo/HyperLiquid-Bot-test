# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T22:29:01.566703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `-0.0511` n `230`; crypto_major avg `-0.0881` n `8`; equity avg `-0.0731` n `96`; fx avg `0.0025` n `6`; index avg `0.0086` n `25`; metal avg `-0.006` n `20`; unknown avg `1.3756` n `770`
- 1h: commodity avg `0.0267` n `12`; crypto_alt avg `-0.0411` n `230`; crypto_major avg `-0.056` n `8`; equity avg `-0.0045` n `96`; fx avg `0.0015` n `6`; index avg `0.0038` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0433` n `770`
- 4h: commodity avg `0.0344` n `12`; crypto_alt avg `0.1593` n `230`; crypto_major avg `0.2312` n `8`; equity avg `-0.0275` n `96`; fx avg `0.0096` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.1894` n `770`
- 24h: commodity avg `0.3621` n `12`; crypto_alt avg `-0.0773` n `230`; crypto_major avg `0.6201` n `8`; equity avg `-0.2013` n `96`; fx avg `-0.0629` n `6`; index avg `0.0472` n `25`; metal avg `-0.0268` n `20`; unknown avg `0.1214` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
