# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T09:29:25.711099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.022` n `232`; crypto_major avg `0.0327` n `8`; equity avg `0.0029` n `134`; fx avg `0.0059` n `6`; index avg `0.0003` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.1402` n `790`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `0.2219` n `232`; crypto_major avg `0.2699` n `8`; equity avg `0.0329` n `134`; fx avg `-0.0005` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0042` n `20`; unknown avg `-0.1435` n `782`
- 4h: commodity avg `-0.0211` n `12`; crypto_alt avg `1.1316` n `232`; crypto_major avg `1.1725` n `8`; equity avg `0.0097` n `134`; fx avg `-0.0103` n `6`; index avg `-0.0054` n `26`; metal avg `0.0053` n `20`; unknown avg `6.1896` n `744`
- 24h: commodity avg `0.1383` n `12`; crypto_alt avg `0.5425` n `232`; crypto_major avg `-1.1437` n `8`; equity avg `0.9845` n `134`; fx avg `-0.1168` n `6`; index avg `0.075` n `26`; metal avg `-0.0878` n `20`; unknown avg `16.4038` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
