# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T05:37:26.943047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.07` n `229`; crypto_major avg `0.1256` n `8`; equity avg `-0.1106` n `91`; fx avg `-0.0163` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0641` n `20`; unknown avg `0.162` n `765`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `0.0613` n `229`; crypto_major avg `0.0236` n `8`; equity avg `-0.2957` n `91`; fx avg `-0.0262` n `6`; index avg `-0.0553` n `25`; metal avg `-0.0943` n `20`; unknown avg `0.2759` n `765`
- 4h: commodity avg `0.0377` n `12`; crypto_alt avg `0.5267` n `229`; crypto_major avg `0.9338` n `8`; equity avg `-0.2515` n `91`; fx avg `-0.0392` n `6`; index avg `-0.0327` n `25`; metal avg `0.0681` n `20`; unknown avg `1.171` n `763`
- 24h: commodity avg `-0.8865` n `12`; crypto_alt avg `1.2422` n `229`; crypto_major avg `1.5084` n `8`; equity avg `1.5811` n `91`; fx avg `0.0451` n `6`; index avg `0.4198` n `25`; metal avg `0.6973` n `20`; unknown avg `0.171` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
