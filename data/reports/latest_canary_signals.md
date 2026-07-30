# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T18:07:34.759935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `0.0787` n `230`; crypto_major avg `0.0069` n `8`; equity avg `-0.1066` n `102`; fx avg `-0.0108` n `6`; index avg `-0.0011` n `25`; metal avg `0.0284` n `20`; unknown avg `0.0139` n `779`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `0.3853` n `230`; crypto_major avg `0.2169` n `8`; equity avg `0.015` n `102`; fx avg `-0.0947` n `6`; index avg `-0.0099` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0349` n `779`
- 4h: commodity avg `0.1789` n `12`; crypto_alt avg `-0.0367` n `230`; crypto_major avg `0.7662` n `8`; equity avg `0.7646` n `102`; fx avg `-0.0496` n `6`; index avg `0.1323` n `25`; metal avg `0.1822` n `20`; unknown avg `0.0118` n `779`
- 24h: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.0606` n `230`; crypto_major avg `0.7448` n `8`; equity avg `3.28` n `102`; fx avg `-0.3836` n `6`; index avg `0.2612` n `25`; metal avg `0.4098` n `20`; unknown avg `-0.1396` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
