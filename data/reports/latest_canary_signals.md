# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T03:37:36.772383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `13`; crypto_alt avg `0.2242` n `239`; crypto_major avg `0.2592` n `8`; equity avg `0.2722` n `158`; fx avg `-0.0032` n `6`; index avg `0.0571` n `27`; metal avg `0.0105` n `20`; unknown avg `-0.1592` n `1260`
- 1h: commodity avg `0.1123` n `13`; crypto_alt avg `-0.4561` n `239`; crypto_major avg `-0.4805` n `8`; equity avg `-0.0461` n `158`; fx avg `0.0151` n `6`; index avg `0.0172` n `27`; metal avg `-0.0393` n `20`; unknown avg `-0.3541` n `1250`
- 4h: commodity avg `0.1497` n `13`; crypto_alt avg `0.6416` n `239`; crypto_major avg `-0.157` n `8`; equity avg `1.2967` n `158`; fx avg `-0.0674` n `6`; index avg `0.2109` n `27`; metal avg `0.4386` n `20`; unknown avg `2.1185` n `1234`
- 24h: commodity avg `0.1244` n `13`; crypto_alt avg `-1.7577` n `239`; crypto_major avg `-2.2535` n `8`; equity avg `0.7975` n `158`; fx avg `-0.0751` n `6`; index avg `0.1039` n `27`; metal avg `0.4913` n `20`; unknown avg `1.2689` n `988`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
