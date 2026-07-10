# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T04:22:27.463645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0277` n `229`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0575` n `91`; fx avg `0.0239` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0345` n `20`; unknown avg `-0.0925` n `765`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `0.0486` n `229`; crypto_major avg `0.2341` n `8`; equity avg `-0.0417` n `91`; fx avg `0.0169` n `6`; index avg `0.0066` n `25`; metal avg `-0.0502` n `20`; unknown avg `-0.1555` n `765`
- 4h: commodity avg `0.1275` n `12`; crypto_alt avg `0.9758` n `229`; crypto_major avg `1.3518` n `8`; equity avg `0.5585` n `91`; fx avg `-0.0317` n `6`; index avg `0.1623` n `25`; metal avg `0.197` n `20`; unknown avg `1.4045` n `763`
- 24h: commodity avg `-0.9843` n `12`; crypto_alt avg `1.6006` n `229`; crypto_major avg `1.8677` n `8`; equity avg `1.8845` n `91`; fx avg `0.0798` n `6`; index avg `0.5085` n `25`; metal avg `0.968` n `20`; unknown avg `0.1901` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
