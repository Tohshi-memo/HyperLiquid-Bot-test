# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T02:07:25.692840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0436` n `100`; fx avg `0.0063` n `6`; index avg `-0.0014` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0367` n `774`
- 1h: commodity avg `0.0702` n `12`; crypto_alt avg `0.1036` n `230`; crypto_major avg `0.0617` n `8`; equity avg `0.0698` n `100`; fx avg `0.0073` n `6`; index avg `0.0236` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0881` n `774`
- 4h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0733` n `230`; crypto_major avg `0.1271` n `8`; equity avg `0.169` n `100`; fx avg `0.0036` n `6`; index avg `0.0435` n `25`; metal avg `0.001` n `20`; unknown avg `-0.2862` n `774`
- 24h: commodity avg `-0.5648` n `12`; crypto_alt avg `0.5775` n `230`; crypto_major avg `1.099` n `8`; equity avg `0.5691` n `100`; fx avg `-0.0229` n `6`; index avg `0.1696` n `25`; metal avg `0.0289` n `20`; unknown avg `-0.2617` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1359`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1236`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `666`, weak_sample_signal
