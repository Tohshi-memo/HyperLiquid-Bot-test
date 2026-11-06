# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T18:37:26.665686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `0.0945` n `239`; crypto_major avg `0.1287` n `8`; equity avg `0.4308` n `158`; fx avg `0.0055` n `6`; index avg `0.0481` n `27`; metal avg `0.0345` n `20`; unknown avg `0.3219` n `1261`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `0.363` n `239`; crypto_major avg `0.4254` n `8`; equity avg `0.5576` n `158`; fx avg `-0.0053` n `6`; index avg `0.0767` n `27`; metal avg `0.1055` n `20`; unknown avg `10.9396` n `1253`
- 4h: commodity avg `0.1679` n `13`; crypto_alt avg `-0.2541` n `239`; crypto_major avg `0.0746` n `8`; equity avg `-0.1867` n `158`; fx avg `-0.0359` n `6`; index avg `-0.0365` n `27`; metal avg `0.1568` n `20`; unknown avg `9.5378` n `1245`
- 24h: commodity avg `0.0398` n `13`; crypto_alt avg `1.9008` n `239`; crypto_major avg `-0.1901` n `8`; equity avg `1.9779` n `158`; fx avg `-0.1217` n `6`; index avg `0.1778` n `27`; metal avg `-0.194` n `20`; unknown avg `42.484` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
