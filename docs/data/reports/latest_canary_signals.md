# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T00:22:25.091384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `-0.2965` n `231`; crypto_major avg `-0.2076` n `8`; equity avg `-0.3631` n `122`; fx avg `0.0006` n `6`; index avg `-0.0635` n `25`; metal avg `-0.1187` n `20`; unknown avg `-0.0182` n `793`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.7784` n `231`; crypto_major avg `-0.5199` n `8`; equity avg `-0.5493` n `122`; fx avg `-0.027` n `6`; index avg `-0.0833` n `25`; metal avg `0.0519` n `20`; unknown avg `0.0002` n `793`
- 4h: commodity avg `-0.1575` n `12`; crypto_alt avg `-0.7968` n `231`; crypto_major avg `0.0213` n `8`; equity avg `-0.4241` n `122`; fx avg `-0.0499` n `6`; index avg `-0.0799` n `25`; metal avg `0.0232` n `20`; unknown avg `0.52` n `793`
- 24h: commodity avg `-0.2834` n `12`; crypto_alt avg `2.3819` n `231`; crypto_major avg `0.7369` n `8`; equity avg `0.2176` n `122`; fx avg `-0.1455` n `6`; index avg `0.0306` n `25`; metal avg `0.1166` n `20`; unknown avg `5.7534` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
