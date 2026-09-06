# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T15:22:31.756378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `0.2015` n `232`; crypto_major avg `0.1892` n `8`; equity avg `0.0276` n `134`; fx avg `0.0064` n `6`; index avg `0.0213` n `26`; metal avg `0.0097` n `20`; unknown avg `1.8362` n `792`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.0716` n `232`; crypto_major avg `0.0523` n `8`; equity avg `-0.0425` n `134`; fx avg `0.0034` n `6`; index avg `0.0044` n `26`; metal avg `0.0113` n `20`; unknown avg `2.4438` n `790`
- 4h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.9278` n `232`; crypto_major avg `-0.5517` n `8`; equity avg `-0.3009` n `134`; fx avg `-0.0192` n `6`; index avg `-0.0452` n `26`; metal avg `-0.0058` n `20`; unknown avg `68.5953` n `720`
- 24h: commodity avg `0.0818` n `12`; crypto_alt avg `1.1893` n `232`; crypto_major avg `0.7997` n `8`; equity avg `0.1833` n `134`; fx avg `-0.0305` n `6`; index avg `0.0243` n `26`; metal avg `-0.003` n `20`; unknown avg `1.8536` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
