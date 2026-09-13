# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T13:52:27.223760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.4483` n `233`; crypto_major avg `0.3927` n `8`; equity avg `0.2606` n `136`; fx avg `-0.0007` n `6`; index avg `0.0383` n `27`; metal avg `0.0064` n `20`; unknown avg `0.2566` n `838`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `0.3339` n `233`; crypto_major avg `0.3015` n `8`; equity avg `0.1922` n `136`; fx avg `-0.0019` n `6`; index avg `0.0457` n `27`; metal avg `-0.0006` n `20`; unknown avg `0.2436` n `836`
- 4h: commodity avg `0.1873` n `12`; crypto_alt avg `0.3953` n `233`; crypto_major avg `0.0838` n `8`; equity avg `-0.0966` n `136`; fx avg `0.0019` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0308` n `20`; unknown avg `0.0635` n `826`
- 24h: commodity avg `0.3018` n `12`; crypto_alt avg `0.0182` n `233`; crypto_major avg `-1.6338` n `8`; equity avg `-1.6949` n `136`; fx avg `0.0027` n `6`; index avg `-0.2649` n `26`; metal avg `-0.0886` n `20`; unknown avg `-0.1151` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
