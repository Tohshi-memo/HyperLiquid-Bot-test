# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T19:22:29.852435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.2963` n `238`; crypto_major avg `-0.1762` n `8`; equity avg `-0.0529` n `156`; fx avg `0.0001` n `6`; index avg `-0.0168` n `27`; metal avg `-0.0196` n `20`; unknown avg `0.4421` n `1255`
- 1h: commodity avg `0.0465` n `13`; crypto_alt avg `-0.5724` n `238`; crypto_major avg `-0.2655` n `8`; equity avg `-0.0792` n `156`; fx avg `0.0045` n `6`; index avg `-0.0305` n `27`; metal avg `-0.0284` n `20`; unknown avg `13.0158` n `1249`
- 4h: commodity avg `-0.0403` n `13`; crypto_alt avg `-1.3062` n `238`; crypto_major avg `-0.626` n `8`; equity avg `-0.2016` n `156`; fx avg `0.0261` n `6`; index avg `-0.0378` n `27`; metal avg `-0.0149` n `20`; unknown avg `0.2774` n `1227`
- 24h: commodity avg `0.0145` n `13`; crypto_alt avg `-1.1325` n `238`; crypto_major avg `-0.47` n `8`; equity avg `0.1972` n `156`; fx avg `0.0204` n `6`; index avg `0.0458` n `27`; metal avg `0.0332` n `20`; unknown avg `4.2164` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
