# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T21:23:01.989739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0674` n `12`; crypto_alt avg `0.1023` n `229`; crypto_major avg `0.0098` n `8`; equity avg `-0.0035` n `92`; fx avg `0.0007` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0296` n `20`; unknown avg `0.065` n `765`
- 1h: commodity avg `-0.0341` n `12`; crypto_alt avg `0.1935` n `229`; crypto_major avg `0.0417` n `8`; equity avg `0.0344` n `92`; fx avg `0.0004` n `6`; index avg `-0.0029` n `25`; metal avg `0.0228` n `20`; unknown avg `-0.2818` n `765`
- 4h: commodity avg `0.0285` n `12`; crypto_alt avg `0.0509` n `229`; crypto_major avg `-0.0099` n `8`; equity avg `-0.1008` n `92`; fx avg `-0.024` n `6`; index avg `0.0398` n `25`; metal avg `0.0524` n `20`; unknown avg `-0.4412` n `765`
- 24h: commodity avg `-0.3244` n `12`; crypto_alt avg `0.723` n `229`; crypto_major avg `0.6658` n `8`; equity avg `-0.6598` n `92`; fx avg `-0.1778` n `6`; index avg `0.04` n `25`; metal avg `0.1624` n `20`; unknown avg `-0.2741` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
