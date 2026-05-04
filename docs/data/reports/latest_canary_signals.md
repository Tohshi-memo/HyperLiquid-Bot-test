# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T07:15:19.046462+00:00`
- Correlation status: `ready`
- Asset price records: `244`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0499` n `7`; crypto_alt avg `0.1076` n `223`; crypto_major avg `0.2116` n `7`; equity avg `0.1076` n `42`; fx avg `-0.0008` n `4`; index avg `0.0454` n `9`; metal avg `0.0647` n `7`; unknown avg `-0.0143` n `314`
- 1h: commodity avg `0.4559` n `7`; crypto_alt avg `0.0907` n `223`; crypto_major avg `-0.036` n `7`; equity avg `0.022` n `42`; fx avg `0.0037` n `4`; index avg `-0.0001` n `9`; metal avg `-0.1527` n `7`; unknown avg `-0.1215` n `314`
- 4h: commodity avg `0.236` n `7`; crypto_alt avg `0.0727` n `223`; crypto_major avg `-0.3407` n `7`; equity avg `-0.3886` n `42`; fx avg `-0.0464` n `4`; index avg `0.0729` n `9`; metal avg `-0.6285` n `7`; unknown avg `-0.4343` n `312`
- 24h: commodity avg `0.3897` n `7`; crypto_alt avg `2.3172` n `223`; crypto_major avg `2.3261` n `7`; equity avg `1.1334` n `42`; fx avg `-0.0267` n `4`; index avg `0.9305` n `9`; metal avg `-0.265` n `7`; unknown avg `-0.175` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3942`, n `236`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3854`, n `236`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3558`, n `240`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3425`, n `240`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.211`, n `236`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1999`, n `236`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1783`, n `240`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `240`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1708`, n `236`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1603`, n `240`, weak_sample_signal
