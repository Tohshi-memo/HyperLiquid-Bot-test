# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T13:50:59.603037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.0321` n `230`; crypto_major avg `0.1262` n `8`; equity avg `-0.0103` n `96`; fx avg `-0.0028` n `6`; index avg `0.0001` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0606` n `770`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.0665` n `230`; crypto_major avg `0.1036` n `8`; equity avg `0.0429` n `96`; fx avg `0.004` n `6`; index avg `-0.0034` n `25`; metal avg `0.0346` n `20`; unknown avg `0.0564` n `770`
- 4h: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.0367` n `230`; crypto_major avg `0.0592` n `8`; equity avg `-0.0254` n `96`; fx avg `0.014` n `6`; index avg `-0.0151` n `25`; metal avg `0.0072` n `20`; unknown avg `0.0247` n `770`
- 24h: commodity avg `0.2153` n `12`; crypto_alt avg `0.5994` n `230`; crypto_major avg `1.2282` n `8`; equity avg `0.2568` n `96`; fx avg `-0.004` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0588` n `20`; unknown avg `0.1715` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1233`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1208`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0897`, n `666`, weak_sample_signal
