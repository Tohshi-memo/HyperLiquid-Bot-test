# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T06:52:28.793074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `0.046` n `231`; crypto_major avg `0.0238` n `8`; equity avg `0.0215` n `127`; fx avg `-0.0137` n `6`; index avg `0.0021` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0268` n `793`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.476` n `231`; crypto_major avg `-0.4029` n `8`; equity avg `0.0126` n `127`; fx avg `-0.0191` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0577` n `761`
- 4h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.2888` n `231`; crypto_major avg `-0.1848` n `8`; equity avg `0.0784` n `127`; fx avg `-0.0087` n `6`; index avg `0.0169` n `26`; metal avg `0.0153` n `20`; unknown avg `-0.0658` n `761`
- 24h: commodity avg `-0.0998` n `12`; crypto_alt avg `-2.4308` n `231`; crypto_major avg `-2.9632` n `8`; equity avg `-1.5017` n `127`; fx avg `-0.0486` n `6`; index avg `-0.1418` n `26`; metal avg `-0.5944` n `20`; unknown avg `-0.4544` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
