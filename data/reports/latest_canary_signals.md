# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T16:07:31.304769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `13`; crypto_alt avg `0.3047` n `237`; crypto_major avg `0.1752` n `8`; equity avg `0.0949` n `152`; fx avg `-0.006` n `6`; index avg `0.018` n `26`; metal avg `-0.0141` n `20`; unknown avg `0.0222` n `1225`
- 1h: commodity avg `0.0808` n `13`; crypto_alt avg `0.2325` n `237`; crypto_major avg `0.1216` n `8`; equity avg `0.1398` n `152`; fx avg `-0.008` n `6`; index avg `0.0311` n `26`; metal avg `0.0595` n `20`; unknown avg `-0.2817` n `1225`
- 4h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.2284` n `237`; crypto_major avg `0.2645` n `8`; equity avg `0.6006` n `152`; fx avg `0.0383` n `6`; index avg `0.1517` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0748` n `1161`
- 24h: commodity avg `0.4295` n `13`; crypto_alt avg `1.0418` n `237`; crypto_major avg `0.4475` n `8`; equity avg `0.8206` n `152`; fx avg `-0.0871` n `6`; index avg `0.0376` n `26`; metal avg `-0.1681` n `20`; unknown avg `-0.6763` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
