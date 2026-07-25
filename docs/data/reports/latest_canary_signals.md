# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T08:22:30.182365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.1972` n `230`; crypto_major avg `0.1597` n `8`; equity avg `0.0048` n `100`; fx avg `0.0002` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.066` n `774`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0857` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `-0.0173` n `100`; fx avg `-0.022` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0739` n `774`
- 4h: commodity avg `0.0674` n `12`; crypto_alt avg `-0.4835` n `230`; crypto_major avg `-0.295` n `8`; equity avg `-0.1227` n `100`; fx avg `0.0223` n `6`; index avg `-0.0116` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.2344` n `758`
- 24h: commodity avg `-0.1214` n `12`; crypto_alt avg `-1.8063` n `230`; crypto_major avg `-1.6271` n `8`; equity avg `-2.7104` n `100`; fx avg `-0.0415` n `6`; index avg `-0.2181` n `25`; metal avg `0.0005` n `20`; unknown avg `13.4415` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1144`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1067`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
