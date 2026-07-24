# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T23:37:26.892563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0573` n `230`; crypto_major avg `-0.0146` n `8`; equity avg `-0.083` n `100`; fx avg `0.0049` n `6`; index avg `-0.0179` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0799` n `774`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0292` n `230`; crypto_major avg `0.0357` n `8`; equity avg `-0.2058` n `100`; fx avg `0.0409` n `6`; index avg `-0.0257` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0875` n `774`
- 4h: commodity avg `0.2816` n `12`; crypto_alt avg `-0.1663` n `230`; crypto_major avg `-0.2577` n `8`; equity avg `-0.2405` n `100`; fx avg `0.0289` n `6`; index avg `-0.045` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0897` n `773`
- 24h: commodity avg `-0.3171` n `12`; crypto_alt avg `-0.9753` n `230`; crypto_major avg `-1.0419` n `8`; equity avg `-3.3413` n `100`; fx avg `-0.1184` n `6`; index avg `-0.4867` n `25`; metal avg `0.0238` n `20`; unknown avg `13.9858` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1275`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1224`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
