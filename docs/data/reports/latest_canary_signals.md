# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T07:07:23.228281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `-0.0175` n `235`; crypto_major avg `-0.0641` n `8`; equity avg `0.0115` n `150`; fx avg `-0.0052` n `6`; index avg `0.0068` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.0617` n `1115`
- 1h: commodity avg `0.018` n `13`; crypto_alt avg `0.5535` n `235`; crypto_major avg `0.1829` n `8`; equity avg `0.0563` n `150`; fx avg `0.0005` n `6`; index avg `0.0079` n `26`; metal avg `0.0148` n `20`; unknown avg `0.8059` n `1115`
- 4h: commodity avg `0.0783` n `13`; crypto_alt avg `0.1177` n `235`; crypto_major avg `-0.1975` n `8`; equity avg `-0.048` n `150`; fx avg `0.006` n `6`; index avg `-0.0066` n `26`; metal avg `0.0037` n `20`; unknown avg `0.0963` n `1093`
- 24h: commodity avg `0.1506` n `13`; crypto_alt avg `1.167` n `235`; crypto_major avg `0.0228` n `8`; equity avg `0.0631` n `150`; fx avg `-0.0051` n `6`; index avg `-0.0117` n `26`; metal avg `0.007` n `20`; unknown avg `0.312` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
