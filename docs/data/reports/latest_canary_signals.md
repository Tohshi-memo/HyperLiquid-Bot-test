# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T05:12:42.720207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0808` n `12`; crypto_alt avg `-0.0398` n `229`; crypto_major avg `-0.1513` n `8`; equity avg `-0.1403` n `91`; fx avg `-0.0239` n `6`; index avg `-0.0219` n `25`; metal avg `-0.008` n `20`; unknown avg `0.1426` n `765`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.044` n `229`; crypto_major avg `-0.1002` n `8`; equity avg `-0.264` n `91`; fx avg `0.0075` n `6`; index avg `-0.0645` n `25`; metal avg `-0.0386` n `20`; unknown avg `0.0049` n `765`
- 4h: commodity avg `0.0882` n `12`; crypto_alt avg `0.8465` n `229`; crypto_major avg `1.16` n `8`; equity avg `0.1285` n `91`; fx avg `0.0073` n `6`; index avg `0.0505` n `25`; metal avg `0.1033` n `20`; unknown avg `2.4192` n `763`
- 24h: commodity avg `-0.9833` n `12`; crypto_alt avg `1.3151` n `229`; crypto_major avg `1.4631` n `8`; equity avg `1.5029` n `91`; fx avg `0.0513` n `6`; index avg `0.3885` n `25`; metal avg `0.905` n `20`; unknown avg `0.1693` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
