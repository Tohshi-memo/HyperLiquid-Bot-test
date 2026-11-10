# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T04:37:30.922042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0488` n `13`; crypto_alt avg `-0.0383` n `239`; crypto_major avg `-0.117` n `8`; equity avg `0.0768` n `160`; fx avg `-0.0085` n `6`; index avg `0.0048` n `27`; metal avg `0.0397` n `20`; unknown avg `-0.1233` n `1261`
- 1h: commodity avg `0.008` n `13`; crypto_alt avg `0.3594` n `239`; crypto_major avg `0.1726` n `8`; equity avg `0.1572` n `160`; fx avg `-0.0169` n `6`; index avg `0.0081` n `27`; metal avg `0.0546` n `20`; unknown avg `0.0406` n `1245`
- 4h: commodity avg `-0.2267` n `13`; crypto_alt avg `0.1526` n `239`; crypto_major avg `-0.3148` n `8`; equity avg `-0.5852` n `160`; fx avg `-0.0038` n `6`; index avg `-0.0843` n `27`; metal avg `0.0568` n `20`; unknown avg `-0.0035` n `1239`
- 24h: commodity avg `-0.8176` n `13`; crypto_alt avg `0.5087` n `239`; crypto_major avg `-0.8811` n `8`; equity avg `3.2347` n `160`; fx avg `0.0137` n `6`; index avg `0.3088` n `27`; metal avg `0.0141` n `20`; unknown avg `187.9154` n `1073`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
