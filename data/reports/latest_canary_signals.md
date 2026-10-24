# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T01:37:27.829289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `-0.4305` n `237`; crypto_major avg `-0.2632` n `8`; equity avg `-0.0997` n `152`; fx avg `-0.0064` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0096` n `20`; unknown avg `2.3383` n `1230`
- 1h: commodity avg `-0.0291` n `13`; crypto_alt avg `0.0752` n `237`; crypto_major avg `0.0545` n `8`; equity avg `-0.0012` n `152`; fx avg `-0.0064` n `6`; index avg `-0.0062` n `26`; metal avg `0.0037` n `20`; unknown avg `3.907` n `1230`
- 4h: commodity avg `0.1168` n `13`; crypto_alt avg `-1.2321` n `237`; crypto_major avg `-1.0166` n `8`; equity avg `-0.2469` n `152`; fx avg `-0.0065` n `6`; index avg `-0.0588` n `26`; metal avg `-0.073` n `20`; unknown avg `4.9085` n `1208`
- 24h: commodity avg `0.458` n `13`; crypto_alt avg `-1.4908` n `237`; crypto_major avg `-0.9733` n `8`; equity avg `0.1835` n `152`; fx avg `-0.0342` n `6`; index avg `-0.0226` n `26`; metal avg `-0.1049` n `20`; unknown avg `205.0001` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
