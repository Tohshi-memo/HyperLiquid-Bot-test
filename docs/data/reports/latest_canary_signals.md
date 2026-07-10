# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T05:22:26.474576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.0015` n `229`; crypto_major avg `0.0306` n `8`; equity avg `0.0179` n `91`; fx avg `0.0157` n `6`; index avg `-0.0049` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.0641` n `765`
- 1h: commodity avg `-0.047` n `12`; crypto_alt avg `-0.0143` n `229`; crypto_major avg `-0.0518` n `8`; equity avg `-0.1889` n `91`; fx avg `-0.0008` n `6`; index avg `-0.0687` n `25`; metal avg `-0.009` n `20`; unknown avg `0.1533` n `765`
- 4h: commodity avg `0.0235` n `12`; crypto_alt avg `0.6233` n `229`; crypto_major avg `0.9599` n `8`; equity avg `0.047` n `91`; fx avg `0.0146` n `6`; index avg `0.0231` n `25`; metal avg `0.0912` n `20`; unknown avg `0.9246` n `763`
- 24h: commodity avg `-1.0061` n `12`; crypto_alt avg `1.3164` n `229`; crypto_major avg `1.4943` n `8`; equity avg `1.5224` n `91`; fx avg `0.0669` n `6`; index avg `0.3832` n `25`; metal avg `0.8999` n `20`; unknown avg `0.1569` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
