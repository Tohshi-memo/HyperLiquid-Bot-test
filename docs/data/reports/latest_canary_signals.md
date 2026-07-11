# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T07:22:23.866783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `-0.046` n `230`; crypto_major avg `0.064` n `8`; equity avg `0.0619` n `92`; fx avg `-0.0032` n `6`; index avg `0.0112` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0763` n `763`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `-0.1724` n `230`; crypto_major avg `-0.0578` n `8`; equity avg `0.134` n `92`; fx avg `-0.0146` n `6`; index avg `0.0288` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.059` n `763`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.1838` n `229`; crypto_major avg `0.0198` n `8`; equity avg `0.1377` n `92`; fx avg `0.0153` n `6`; index avg `0.021` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0709` n `731`
- 24h: commodity avg `-0.1364` n `12`; crypto_alt avg `0.3834` n `229`; crypto_major avg `-0.133` n `8`; equity avg `0.1953` n `92`; fx avg `-0.076` n `6`; index avg `0.1861` n `25`; metal avg `-0.0025` n `20`; unknown avg `2.8367` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
