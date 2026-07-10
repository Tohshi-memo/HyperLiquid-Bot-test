# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T00:52:30.828126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `-0.0094` n `229`; crypto_major avg `-0.0397` n `8`; equity avg `0.2203` n `91`; fx avg `-0.0318` n `6`; index avg `0.0283` n `25`; metal avg `0.0464` n `20`; unknown avg `1.3022` n `765`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.1724` n `229`; crypto_major avg `-0.197` n `8`; equity avg `-0.3236` n `91`; fx avg `0.0232` n `6`; index avg `-0.129` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0859` n `765`
- 4h: commodity avg `0.04` n `12`; crypto_alt avg `-0.4101` n `229`; crypto_major avg `-0.3564` n `8`; equity avg `-0.1389` n `91`; fx avg `0.0377` n `6`; index avg `-0.0977` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.4436` n `765`
- 24h: commodity avg `-1.0497` n `12`; crypto_alt avg `0.7701` n `229`; crypto_major avg `0.2601` n `8`; equity avg `0.9937` n `91`; fx avg `0.0556` n `6`; index avg `0.1977` n `25`; metal avg `0.6543` n `20`; unknown avg `-0.2114` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
