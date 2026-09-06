# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T13:37:27.497085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0606` n `232`; crypto_major avg `-0.0338` n `8`; equity avg `-0.0305` n `134`; fx avg `0.0129` n `6`; index avg `-0.0123` n `26`; metal avg `0.0002` n `20`; unknown avg `0.0601` n `776`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.2619` n `232`; crypto_major avg `-0.4314` n `8`; equity avg `-0.1746` n `134`; fx avg `0.0068` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.2854` n `726`
- 4h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.2086` n `232`; crypto_major avg `-0.2768` n `8`; equity avg `-0.0229` n `134`; fx avg `0.0197` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0175` n `20`; unknown avg `66.7209` n `720`
- 24h: commodity avg `0.0811` n `12`; crypto_alt avg `1.7982` n `232`; crypto_major avg `1.1386` n `8`; equity avg `0.3746` n `134`; fx avg `-0.0208` n `6`; index avg `0.0609` n `26`; metal avg `0.0075` n `20`; unknown avg `0.298` n `624`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
