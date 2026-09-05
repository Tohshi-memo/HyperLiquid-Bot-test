# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T20:29:59.663291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.0708` n `232`; crypto_major avg `-0.208` n `8`; equity avg `-0.0599` n `134`; fx avg `0.0028` n `6`; index avg `-0.0263` n `26`; metal avg `0.0001` n `20`; unknown avg `0.3314` n `776`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1259` n `232`; crypto_major avg `-0.3407` n `8`; equity avg `0.0033` n `134`; fx avg `-0.0117` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0049` n `20`; unknown avg `1.1052` n `774`
- 4h: commodity avg `0.0531` n `12`; crypto_alt avg `0.4071` n `232`; crypto_major avg `0.4895` n `8`; equity avg `0.0404` n `134`; fx avg `-0.015` n `6`; index avg `0.026` n `26`; metal avg `0.0199` n `20`; unknown avg `1.3954` n `774`
- 24h: commodity avg `0.1308` n `12`; crypto_alt avg `2.7812` n `232`; crypto_major avg `2.2837` n `8`; equity avg `0.19` n `134`; fx avg `-0.03` n `6`; index avg `0.0112` n `26`; metal avg `0.0368` n `20`; unknown avg `334.3838` n `662`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
