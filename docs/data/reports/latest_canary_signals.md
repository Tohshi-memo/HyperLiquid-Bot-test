# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T20:26:23.599560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0526` n `13`; crypto_alt avg `-0.3519` n `237`; crypto_major avg `-0.0582` n `8`; equity avg `0.0932` n `152`; fx avg `-0.003` n `6`; index avg `0.0198` n `26`; metal avg `0.0014` n `20`; unknown avg `0.0181` n `1178`
- 1h: commodity avg `0.0395` n `13`; crypto_alt avg `-0.4476` n `237`; crypto_major avg `0.0` n `8`; equity avg `-0.0567` n `152`; fx avg `-0.0173` n `6`; index avg `0.013` n `26`; metal avg `-0.0233` n `20`; unknown avg `109.7528` n `1150`
- 4h: commodity avg `0.0127` n `13`; crypto_alt avg `-1.4263` n `237`; crypto_major avg `-0.7419` n `8`; equity avg `-0.4039` n `152`; fx avg `-0.0355` n `6`; index avg `-0.0446` n `26`; metal avg `-0.1206` n `20`; unknown avg `0.1598` n `1123`
- 24h: commodity avg `0.4017` n `13`; crypto_alt avg `-0.0222` n `237`; crypto_major avg `0.2247` n `8`; equity avg `1.1153` n `152`; fx avg `-0.092` n `6`; index avg `0.0623` n `26`; metal avg `-0.1266` n `20`; unknown avg `-0.1421` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
