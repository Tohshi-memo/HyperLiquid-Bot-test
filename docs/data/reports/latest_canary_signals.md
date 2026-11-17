# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T07:22:28.099791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `0.037` n `239`; crypto_major avg `-0.0285` n `8`; equity avg `-0.0012` n `162`; fx avg `0.0062` n `6`; index avg `-0.0203` n `27`; metal avg `-0.0018` n `20`; unknown avg `200.8541` n `1250`
- 1h: commodity avg `-0.0087` n `13`; crypto_alt avg `0.2092` n `239`; crypto_major avg `0.1206` n `8`; equity avg `0.2043` n `162`; fx avg `-0.0094` n `6`; index avg `0.0127` n `27`; metal avg `0.0358` n `20`; unknown avg `205.7343` n `1214`
- 4h: commodity avg `0.01` n `13`; crypto_alt avg `0.1126` n `239`; crypto_major avg `0.1519` n `8`; equity avg `-0.8145` n `162`; fx avg `-0.029` n `6`; index avg `-0.0973` n `27`; metal avg `-0.0662` n `20`; unknown avg `-0.3391` n `1188`
- 24h: commodity avg `-1.1997` n `13`; crypto_alt avg `1.1599` n `239`; crypto_major avg `1.4044` n `8`; equity avg `-2.3967` n `162`; fx avg `-0.0246` n `6`; index avg `-0.2473` n `27`; metal avg `-0.0023` n `20`; unknown avg `232.9745` n `1101`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
