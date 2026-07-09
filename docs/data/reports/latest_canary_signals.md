# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T03:07:26.823144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.0363` n `229`; crypto_major avg `0.0316` n `8`; equity avg `-0.1234` n `91`; fx avg `0.0025` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0632` n `20`; unknown avg `-0.0458` n `764`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `-0.4301` n `229`; crypto_major avg `-0.4466` n `8`; equity avg `-0.5681` n `91`; fx avg `-0.001` n `6`; index avg `-0.1184` n `25`; metal avg `-0.1949` n `20`; unknown avg `-0.3272` n `764`
- 4h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.3471` n `229`; crypto_major avg `-0.5482` n `8`; equity avg `-0.2942` n `91`; fx avg `0.0258` n `6`; index avg `-0.1753` n `25`; metal avg `-0.1555` n `20`; unknown avg `-0.1543` n `764`
- 24h: commodity avg `0.3329` n `12`; crypto_alt avg `-0.8225` n `229`; crypto_major avg `-1.4949` n `8`; equity avg `0.2643` n `91`; fx avg `0.0564` n `6`; index avg `-0.2755` n `25`; metal avg `-1.0701` n `20`; unknown avg `0.0427` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
