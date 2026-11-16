# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T15:07:27.576617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `13`; crypto_alt avg `-0.9982` n `239`; crypto_major avg `-1.1504` n `8`; equity avg `-0.7814` n `162`; fx avg `-0.0122` n `6`; index avg `-0.077` n `27`; metal avg `-0.1397` n `20`; unknown avg `0.0853` n `1257`
- 1h: commodity avg `-0.1691` n `13`; crypto_alt avg `0.3984` n `239`; crypto_major avg `0.523` n `8`; equity avg `-0.7401` n `162`; fx avg `-0.0166` n `6`; index avg `-0.0798` n `27`; metal avg `-0.0519` n `20`; unknown avg `-0.2547` n `1253`
- 4h: commodity avg `-0.4939` n `13`; crypto_alt avg `-0.3977` n `239`; crypto_major avg `-0.5856` n `8`; equity avg `-1.5112` n `162`; fx avg `0.0121` n `6`; index avg `-0.1534` n `27`; metal avg `-0.1331` n `20`; unknown avg `2.5329` n `1243`
- 24h: commodity avg `-0.7707` n `13`; crypto_alt avg `-0.0545` n `239`; crypto_major avg `0.0325` n `8`; equity avg `-1.9452` n `162`; fx avg `-0.0269` n `6`; index avg `-0.1771` n `27`; metal avg `-0.0229` n `20`; unknown avg `227.7333` n `1050`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
