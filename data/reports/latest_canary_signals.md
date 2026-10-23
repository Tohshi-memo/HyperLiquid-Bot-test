# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T20:22:28.947473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0524` n `13`; crypto_alt avg `-0.2127` n `237`; crypto_major avg `-0.0117` n `8`; equity avg `0.0874` n `152`; fx avg `-0.001` n `6`; index avg `0.021` n `26`; metal avg `-0.0028` n `20`; unknown avg `7.7033` n `1192`
- 1h: commodity avg `0.0397` n `13`; crypto_alt avg `-0.3089` n `237`; crypto_major avg `0.0465` n `8`; equity avg `-0.0626` n `152`; fx avg `-0.0153` n `6`; index avg `0.0141` n `26`; metal avg `-0.0275` n `20`; unknown avg `110.5376` n `1164`
- 4h: commodity avg `0.013` n `13`; crypto_alt avg `-1.2901` n `237`; crypto_major avg `-0.6959` n `8`; equity avg `-0.4099` n `152`; fx avg `-0.0335` n `6`; index avg `-0.0435` n `26`; metal avg `-0.1248` n `20`; unknown avg `2.5292` n `1137`
- 24h: commodity avg `0.4019` n `13`; crypto_alt avg `0.1181` n `237`; crypto_major avg `0.2712` n `8`; equity avg `1.1087` n `152`; fx avg `-0.09` n `6`; index avg `0.0635` n `26`; metal avg `-0.1308` n `20`; unknown avg `-0.119` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
