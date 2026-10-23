# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T23:37:30.564015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `13`; crypto_alt avg `-0.0131` n `237`; crypto_major avg `-0.049` n `8`; equity avg `-0.0022` n `152`; fx avg `0.0011` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0105` n `20`; unknown avg `1.8857` n `1228`
- 1h: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.3471` n `237`; crypto_major avg `-0.2217` n `8`; equity avg `-0.0969` n `152`; fx avg `-0.0413` n `6`; index avg `-0.0173` n `26`; metal avg `-0.021` n `20`; unknown avg `0.3529` n `1226`
- 4h: commodity avg `0.0674` n `13`; crypto_alt avg `-1.6074` n `237`; crypto_major avg `-0.76` n `8`; equity avg `-0.2094` n `152`; fx avg `0.0011` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0844` n `20`; unknown avg `109.4882` n `1130`
- 24h: commodity avg `0.4244` n `13`; crypto_alt avg `-0.7991` n `237`; crypto_major avg `-0.3309` n `8`; equity avg `1.4941` n `152`; fx avg `-0.0638` n `6`; index avg `0.1003` n `26`; metal avg `-0.1752` n `20`; unknown avg `200.3598` n `1020`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
