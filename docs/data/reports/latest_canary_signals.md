# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T15:52:34.185366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `13`; crypto_alt avg `-0.1433` n `239`; crypto_major avg `-0.1518` n `8`; equity avg `0.0026` n `158`; fx avg `0.0026` n `6`; index avg `-0.01` n `27`; metal avg `-0.0152` n `20`; unknown avg `0.7367` n `1259`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `-0.5846` n `239`; crypto_major avg `-0.4958` n `8`; equity avg `-0.1543` n `158`; fx avg `0.0039` n `6`; index avg `0.0016` n `27`; metal avg `-0.0298` n `20`; unknown avg `163.9642` n `1247`
- 4h: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.5569` n `239`; crypto_major avg `-0.608` n `8`; equity avg `-0.1364` n `158`; fx avg `0.0059` n `6`; index avg `0.0239` n `27`; metal avg `-0.0236` n `20`; unknown avg `-0.0227` n `1241`
- 24h: commodity avg `0.3888` n `13`; crypto_alt avg `-1.9661` n `239`; crypto_major avg `-0.9941` n `8`; equity avg `-0.0402` n `158`; fx avg `-0.004` n `6`; index avg `-0.0565` n `27`; metal avg `0.0176` n `20`; unknown avg `-0.435` n `1113`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
