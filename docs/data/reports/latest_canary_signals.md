# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T15:22:34.378273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.65` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.867` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.1721` n `230`; crypto_major avg `-0.1089` n `8`; equity avg `-0.343` n `102`; fx avg `-0.013` n `6`; index avg `-0.0353` n `25`; metal avg `0.0085` n `20`; unknown avg `0.0963` n `778`
- 1h: commodity avg `0.1763` n `12`; crypto_alt avg `-0.416` n `230`; crypto_major avg `-0.2585` n `8`; equity avg `-0.8792` n `102`; fx avg `-0.0064` n `6`; index avg `-0.1491` n `25`; metal avg `-0.0341` n `20`; unknown avg `-0.0536` n `778`
- 4h: commodity avg `0.5103` n `12`; crypto_alt avg `-0.7079` n `230`; crypto_major avg `-0.6047` n `8`; equity avg `-2.4717` n `102`; fx avg `-0.0111` n `6`; index avg `-0.4195` n `25`; metal avg `-0.1618` n `20`; unknown avg `0.7443` n `777`
- 24h: commodity avg `1.2169` n `12`; crypto_alt avg `-2.4248` n `230`; crypto_major avg `-0.2591` n `8`; equity avg `-1.7582` n `102`; fx avg `-0.0649` n `6`; index avg `-0.4497` n `25`; metal avg `-0.2719` n `20`; unknown avg `-0.0426` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
