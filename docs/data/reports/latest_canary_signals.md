# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T10:52:55.063151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1579` n `12`; crypto_alt avg `-0.1362` n `229`; crypto_major avg `-0.2116` n `8`; equity avg `-0.2183` n `91`; fx avg `-0.0006` n `6`; index avg `-0.0637` n `25`; metal avg `-0.0848` n `20`; unknown avg `0.042` n `764`
- 1h: commodity avg `0.3049` n `12`; crypto_alt avg `-0.1827` n `229`; crypto_major avg `-0.3002` n `8`; equity avg `-0.2743` n `91`; fx avg `-0.0123` n `6`; index avg `-0.0601` n `25`; metal avg `-0.1981` n `20`; unknown avg `0.0433` n `764`
- 4h: commodity avg `0.1767` n `12`; crypto_alt avg `-0.4531` n `229`; crypto_major avg `-0.6279` n `8`; equity avg `-0.1013` n `91`; fx avg `0.0009` n `6`; index avg `-0.058` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.1773` n `764`
- 24h: commodity avg `-0.1206` n `12`; crypto_alt avg `1.5072` n `229`; crypto_major avg `0.4414` n `8`; equity avg `2.9844` n `91`; fx avg `0.1571` n `6`; index avg `0.4249` n `25`; metal avg `0.5019` n `20`; unknown avg `0.717` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
