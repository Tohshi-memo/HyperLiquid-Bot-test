# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T00:52:26.860239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.019` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.081` n `237`; crypto_major avg `0.0772` n `8`; equity avg `-0.0154` n `152`; fx avg `-0.005` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.1982` n `1230`
- 1h: commodity avg `0.0669` n `13`; crypto_alt avg `-0.2967` n `237`; crypto_major avg `-0.4328` n `8`; equity avg `-0.0942` n `152`; fx avg `-0.0045` n `6`; index avg `-0.0168` n `26`; metal avg `-0.0366` n `20`; unknown avg `2.0991` n `1224`
- 4h: commodity avg `0.1787` n `13`; crypto_alt avg `-1.3399` n `237`; crypto_major avg `-1.082` n `8`; equity avg `-0.2977` n `152`; fx avg `0.0117` n `6`; index avg `-0.063` n `26`; metal avg `-0.0568` n `20`; unknown avg `0.471` n `1202`
- 24h: commodity avg `0.6269` n `13`; crypto_alt avg `-1.0538` n `237`; crypto_major avg `-0.8544` n `8`; equity avg `0.5725` n `152`; fx avg `-0.0203` n `6`; index avg `0.0016` n `26`; metal avg `-0.2223` n `20`; unknown avg `200.3139` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
