# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T15:07:24.572155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.2481` n `232`; crypto_major avg `-0.2846` n `8`; equity avg `-0.0545` n `134`; fx avg `-0.0184` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0132` n `20`; unknown avg `147.8576` n `790`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `-0.9007` n `232`; crypto_major avg `-0.6556` n `8`; equity avg `-0.1471` n `134`; fx avg `-0.0196` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0084` n `20`; unknown avg `146.7565` n `790`
- 4h: commodity avg `0.0218` n `12`; crypto_alt avg `-1.0524` n `232`; crypto_major avg `-0.7141` n `8`; equity avg `-0.327` n `134`; fx avg `-0.0106` n `6`; index avg `-0.0636` n `26`; metal avg `-0.0142` n `20`; unknown avg `67.5811` n `720`
- 24h: commodity avg `0.13` n `12`; crypto_alt avg `0.818` n `232`; crypto_major avg `0.547` n `8`; equity avg `0.1568` n `134`; fx avg `-0.0446` n `6`; index avg `0.003` n `26`; metal avg `-0.0069` n `20`; unknown avg `1.4297` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
