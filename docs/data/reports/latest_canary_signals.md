# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T09:22:33.482976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `13`; crypto_alt avg `0.2285` n `239`; crypto_major avg `0.009` n `8`; equity avg `-0.0636` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0187` n `20`; unknown avg `-0.04` n `1263`
- 1h: commodity avg `-0.2931` n `13`; crypto_alt avg `-0.0017` n `239`; crypto_major avg `-0.3553` n `8`; equity avg `-0.3634` n `162`; fx avg `-0.0084` n `6`; index avg `-0.0275` n `27`; metal avg `0.0166` n `20`; unknown avg `8.6514` n `1259`
- 4h: commodity avg `-0.1816` n `13`; crypto_alt avg `-0.7484` n `239`; crypto_major avg `-0.9724` n `8`; equity avg `-0.6328` n `162`; fx avg `-0.0083` n `6`; index avg `-0.012` n `27`; metal avg `-0.1082` n `20`; unknown avg `13.6696` n `1077`
- 24h: commodity avg `-0.5132` n `13`; crypto_alt avg `-1.3901` n `239`; crypto_major avg `-1.6345` n `8`; equity avg `-0.9174` n `162`; fx avg `-0.0437` n `6`; index avg `-0.0403` n `27`; metal avg `0.0035` n `20`; unknown avg `13.9575` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
