# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T15:52:26.366096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.2754` n `232`; crypto_major avg `0.0349` n `8`; equity avg `0.0106` n `134`; fx avg `0.0145` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.8578` n `792`
- 1h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.3151` n `232`; crypto_major avg `-0.0977` n `8`; equity avg `0.0306` n `134`; fx avg `-0.0038` n `6`; index avg `0.0232` n `26`; metal avg `-0.0113` n `20`; unknown avg `147.4042` n `790`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `-0.7115` n `232`; crypto_major avg `-0.6165` n `8`; equity avg `-0.2332` n `134`; fx avg `0.0132` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0194` n `20`; unknown avg `67.603` n `720`
- 24h: commodity avg `0.0876` n `12`; crypto_alt avg `1.6136` n `232`; crypto_major avg `0.7226` n `8`; equity avg `0.2326` n `134`; fx avg `-0.0178` n `6`; index avg `0.035` n `26`; metal avg `-0.0164` n `20`; unknown avg `1.8206` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
