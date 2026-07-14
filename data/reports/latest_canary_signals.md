# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T03:37:29.944859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `0.3021` n `230`; crypto_major avg `0.4013` n `8`; equity avg `0.367` n `92`; fx avg `-0.0237` n `6`; index avg `0.1258` n `25`; metal avg `0.08` n `20`; unknown avg `0.2598` n `766`
- 1h: commodity avg `0.1712` n `12`; crypto_alt avg `-0.0172` n `230`; crypto_major avg `0.0461` n `8`; equity avg `-0.1806` n `92`; fx avg `-0.0729` n `6`; index avg `-0.0087` n `25`; metal avg `0.0384` n `20`; unknown avg `-0.1791` n `766`
- 4h: commodity avg `0.087` n `12`; crypto_alt avg `0.2183` n `230`; crypto_major avg `0.2399` n `8`; equity avg `-0.1555` n `92`; fx avg `-0.0796` n `6`; index avg `-0.1083` n `25`; metal avg `0.1475` n `20`; unknown avg `-0.1696` n `766`
- 24h: commodity avg `1.0623` n `12`; crypto_alt avg `-0.2822` n `230`; crypto_major avg `-0.8333` n `8`; equity avg `-1.7019` n `92`; fx avg `-0.2291` n `6`; index avg `-0.3785` n `25`; metal avg `0.027` n `20`; unknown avg `-0.2637` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
