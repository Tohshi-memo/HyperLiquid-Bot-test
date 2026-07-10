# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T02:22:28.567928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0038` n `229`; crypto_major avg `0.0523` n `8`; equity avg `-0.0513` n `91`; fx avg `-0.041` n `6`; index avg `-0.0405` n `25`; metal avg `0.054` n `20`; unknown avg `-0.0275` n `765`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `0.5769` n `229`; crypto_major avg `0.7566` n `8`; equity avg `0.0219` n `91`; fx avg `-0.0403` n `6`; index avg `-0.0171` n `25`; metal avg `0.0691` n `20`; unknown avg `0.3286` n `763`
- 4h: commodity avg `0.1025` n `12`; crypto_alt avg `0.6473` n `229`; crypto_major avg `0.7911` n `8`; equity avg `-0.0021` n `91`; fx avg `-0.0372` n `6`; index avg `-0.0849` n `25`; metal avg `0.1484` n `20`; unknown avg `0.1136` n `763`
- 24h: commodity avg `-1.0031` n `12`; crypto_alt avg `1.4293` n `229`; crypto_major avg `1.4525` n `8`; equity avg `1.0644` n `91`; fx avg `-0.0043` n `6`; index avg `0.2326` n `25`; metal avg `0.6723` n `20`; unknown avg `-0.0288` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
