# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T01:07:30.357891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0414` n `13`; crypto_alt avg `0.1191` n `237`; crypto_major avg `0.06` n `8`; equity avg `0.0825` n `152`; fx avg `0.0` n `6`; index avg `0.0145` n `26`; metal avg `0.0143` n `20`; unknown avg `4.14` n `1228`
- 1h: commodity avg `-0.012` n `13`; crypto_alt avg `-0.1747` n `237`; crypto_major avg `-0.3546` n `8`; equity avg `-0.1191` n `152`; fx avg `-0.0072` n `6`; index avg `-0.0237` n `26`; metal avg `-0.0164` n `20`; unknown avg `3.9394` n `1230`
- 4h: commodity avg `0.1101` n `13`; crypto_alt avg `-1.3108` n `237`; crypto_major avg `-1.0236` n `8`; equity avg `-0.2265` n `152`; fx avg `0.0053` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0574` n `20`; unknown avg `4.4693` n `1208`
- 24h: commodity avg `0.4593` n `13`; crypto_alt avg `-0.8795` n `237`; crypto_major avg `-0.6345` n `8`; equity avg `0.7007` n `152`; fx avg `0.0021` n `6`; index avg `0.0219` n `26`; metal avg `-0.1215` n `20`; unknown avg `205.0841` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
