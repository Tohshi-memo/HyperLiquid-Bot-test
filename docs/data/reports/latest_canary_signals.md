# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T04:37:25.209519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.0057` n `229`; crypto_major avg `0.0503` n `8`; equity avg `-0.0031` n `91`; fx avg `0.0092` n `6`; index avg `-0.0155` n `25`; metal avg `0.0213` n `20`; unknown avg `0.1461` n `765`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.0029` n `229`; crypto_major avg `0.1675` n `8`; equity avg `0.0783` n `91`; fx avg `0.0162` n `6`; index avg `0.0159` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.221` n `765`
- 4h: commodity avg `0.0715` n `12`; crypto_alt avg `1.0496` n `229`; crypto_major avg `1.4774` n `8`; equity avg `0.6236` n `91`; fx avg `-0.0274` n `6`; index avg `0.1563` n `25`; metal avg `0.2363` n `20`; unknown avg `2.613` n `763`
- 24h: commodity avg `-1.0098` n `12`; crypto_alt avg `1.326` n `229`; crypto_major avg `1.5983` n `8`; equity avg `1.7154` n `91`; fx avg `0.0769` n `6`; index avg `0.4384` n `25`; metal avg `0.9312` n `20`; unknown avg `0.1595` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
