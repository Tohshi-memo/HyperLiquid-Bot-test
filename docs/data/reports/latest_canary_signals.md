# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T14:22:38.525218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `0.1109` n `235`; crypto_major avg `0.1375` n `8`; equity avg `-0.0841` n `150`; fx avg `-0.016` n `6`; index avg `-0.0441` n `26`; metal avg `-0.0762` n `20`; unknown avg `2.8444` n `1052`
- 1h: commodity avg `0.0147` n `13`; crypto_alt avg `-0.2267` n `235`; crypto_major avg `0.121` n `8`; equity avg `0.2924` n `150`; fx avg `-0.0124` n `6`; index avg `-0.0081` n `26`; metal avg `-0.1584` n `20`; unknown avg `151.8732` n `1050`
- 4h: commodity avg `0.1369` n `13`; crypto_alt avg `-0.1633` n `235`; crypto_major avg `0.1554` n `8`; equity avg `0.4552` n `150`; fx avg `0.0237` n `6`; index avg `0.0564` n `26`; metal avg `-0.1196` n `20`; unknown avg `10.1801` n `1044`
- 24h: commodity avg `-0.3088` n `13`; crypto_alt avg `-0.512` n `235`; crypto_major avg `-0.1989` n `8`; equity avg `0.9477` n `149`; fx avg `0.1373` n `6`; index avg `0.1439` n `26`; metal avg `-0.2141` n `20`; unknown avg `1.3855` n `864`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
