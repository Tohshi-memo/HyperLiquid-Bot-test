# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T13:37:37.704534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1829` n `13`; crypto_alt avg `0.33` n `237`; crypto_major avg `0.2121` n `8`; equity avg `0.1072` n `151`; fx avg `-0.0052` n `6`; index avg `0.0321` n `26`; metal avg `0.039` n `20`; unknown avg `48.6016` n `1194`
- 1h: commodity avg `-0.1621` n `13`; crypto_alt avg `0.2924` n `237`; crypto_major avg `0.2526` n `8`; equity avg `0.3862` n `151`; fx avg `0.0232` n `6`; index avg `0.1051` n `26`; metal avg `0.1355` n `20`; unknown avg `15.2488` n `1190`
- 4h: commodity avg `-0.3015` n `13`; crypto_alt avg `0.7591` n `237`; crypto_major avg `0.5865` n `8`; equity avg `0.073` n `151`; fx avg `0.0319` n `6`; index avg `0.061` n `26`; metal avg `0.0151` n `20`; unknown avg `11.0329` n `1182`
- 24h: commodity avg `0.1317` n `13`; crypto_alt avg `0.4813` n `237`; crypto_major avg `-0.2322` n `8`; equity avg `-2.0791` n `151`; fx avg `-0.0054` n `6`; index avg `-0.2519` n `26`; metal avg `-0.1812` n `20`; unknown avg `4.4564` n `1063`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
