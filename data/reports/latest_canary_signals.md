# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T18:37:37.312980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.41` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.9301` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `-0.2511` n `228`; crypto_major avg `-0.3451` n `8`; equity avg `-0.0092` n `88`; fx avg `0.0032` n `6`; index avg `-0.0005` n `23`; metal avg `-0.0293` n `20`; unknown avg `-0.0099` n `765`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.3455` n `228`; crypto_major avg `-0.1873` n `8`; equity avg `0.1529` n `88`; fx avg `-0.009` n `6`; index avg `0.0373` n `23`; metal avg `0.2883` n `20`; unknown avg `0.1487` n `765`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `1.2198` n `228`; crypto_major avg `1.9654` n `8`; equity avg `1.8956` n `88`; fx avg `-0.0083` n `6`; index avg `0.2605` n `23`; metal avg `0.0353` n `20`; unknown avg `1.4341` n `764`
- 24h: commodity avg `-0.5422` n `12`; crypto_alt avg `1.801` n `228`; crypto_major avg `2.6694` n `8`; equity avg `1.5054` n `88`; fx avg `0.1343` n `6`; index avg `0.1647` n `23`; metal avg `-0.4347` n `20`; unknown avg `1.4711` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
