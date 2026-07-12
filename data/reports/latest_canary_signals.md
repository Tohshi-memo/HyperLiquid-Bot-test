# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T14:52:27.005501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.2166` n `230`; crypto_major avg `0.2496` n `8`; equity avg `0.0111` n `92`; fx avg `-0.0036` n `6`; index avg `0.0011` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0032` n `765`
- 1h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.1656` n `230`; crypto_major avg `0.2901` n `8`; equity avg `0.0` n `92`; fx avg `0.0014` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0009` n `765`
- 4h: commodity avg `-0.075` n `12`; crypto_alt avg `0.2468` n `230`; crypto_major avg `0.7618` n `8`; equity avg `0.1043` n `92`; fx avg `0.0017` n `6`; index avg `0.0182` n `25`; metal avg `-0.0197` n `20`; unknown avg `-0.1622` n `763`
- 24h: commodity avg `0.428` n `12`; crypto_alt avg `-1.1906` n `230`; crypto_major avg `-0.6136` n `8`; equity avg `-0.0401` n `92`; fx avg `0.0189` n `6`; index avg `-0.1098` n `25`; metal avg `-0.1319` n `20`; unknown avg `0.1205` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
