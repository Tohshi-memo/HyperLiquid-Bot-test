# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:07:29.757971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.0225` n `230`; crypto_major avg `-0.0362` n `8`; equity avg `0.0039` n `112`; fx avg `-0.0014` n `6`; index avg `0.0026` n `25`; metal avg `0.0011` n `20`; unknown avg `0.4137` n `784`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `-0.0381` n `230`; crypto_major avg `-0.1978` n `8`; equity avg `-0.0104` n `112`; fx avg `0.0048` n `6`; index avg `0.0001` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.4518` n `784`
- 4h: commodity avg `0.1283` n `12`; crypto_alt avg `0.396` n `230`; crypto_major avg `-0.1859` n `8`; equity avg `0.1709` n `112`; fx avg `0.0007` n `6`; index avg `0.0153` n `25`; metal avg `0.0233` n `20`; unknown avg `0.5524` n `784`
- 24h: commodity avg `0.0595` n `12`; crypto_alt avg `1.4262` n `230`; crypto_major avg `1.3355` n `8`; equity avg `0.6932` n `112`; fx avg `0.0119` n `6`; index avg `0.0116` n `25`; metal avg `0.0312` n `20`; unknown avg `0.1948` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
