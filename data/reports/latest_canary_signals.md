# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T08:52:27.814411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0954` n `232`; crypto_major avg `0.096` n `8`; equity avg `-0.0027` n `134`; fx avg `-0.019` n `6`; index avg `0.0017` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.2565` n `790`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `0.0739` n `232`; crypto_major avg `0.2649` n `8`; equity avg `-0.0055` n `134`; fx avg `-0.0137` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0184` n `20`; unknown avg `0.341` n `782`
- 4h: commodity avg `-0.0499` n `12`; crypto_alt avg `1.0158` n `232`; crypto_major avg `1.0281` n `8`; equity avg `0.0781` n `134`; fx avg `-0.0251` n `6`; index avg `0.005` n `26`; metal avg `0.0111` n `20`; unknown avg `16.254` n `746`
- 24h: commodity avg `0.1565` n `12`; crypto_alt avg `0.7715` n `232`; crypto_major avg `-1.0948` n `8`; equity avg `0.9167` n `134`; fx avg `-0.1417` n `6`; index avg `0.0624` n `26`; metal avg `-0.2223` n `20`; unknown avg `16.6593` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
