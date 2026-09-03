# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T02:22:26.417274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `0.169` n `232`; crypto_major avg `0.2962` n `8`; equity avg `0.1343` n `133`; fx avg `-0.0214` n `6`; index avg `0.0198` n `26`; metal avg `0.0026` n `20`; unknown avg `0.2797` n `792`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `-0.0029` n `232`; crypto_major avg `0.1898` n `8`; equity avg `0.0824` n `133`; fx avg `-0.0309` n `6`; index avg `0.0071` n `26`; metal avg `0.0948` n `20`; unknown avg `-0.0368` n `790`
- 4h: commodity avg `0.0993` n `12`; crypto_alt avg `1.0105` n `232`; crypto_major avg `0.8838` n `8`; equity avg `0.1409` n `133`; fx avg `-0.0607` n `6`; index avg `-0.009` n `26`; metal avg `0.1476` n `20`; unknown avg `0.28` n `790`
- 24h: commodity avg `0.1533` n `12`; crypto_alt avg `0.7039` n `232`; crypto_major avg `0.5616` n `8`; equity avg `1.3733` n `133`; fx avg `-0.3912` n `6`; index avg `0.1311` n `26`; metal avg `0.8247` n `20`; unknown avg `-0.3472` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
