# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T23:22:27.514016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0544` n `13`; crypto_alt avg `0.6488` n `237`; crypto_major avg `0.3336` n `8`; equity avg `0.1244` n `152`; fx avg `0.006` n `6`; index avg `0.0039` n `26`; metal avg `0.036` n `20`; unknown avg `2.0363` n `1230`
- 1h: commodity avg `0.0204` n `13`; crypto_alt avg `-1.2281` n `237`; crypto_major avg `-0.7572` n `8`; equity avg `-0.2399` n `152`; fx avg `-0.004` n `6`; index avg `-0.0512` n `26`; metal avg `-0.0392` n `20`; unknown avg `2.2528` n `1230`
- 4h: commodity avg `0.1616` n `13`; crypto_alt avg `-1.425` n `237`; crypto_major avg `-0.5739` n `8`; equity avg `-0.3086` n `152`; fx avg `0.0332` n `6`; index avg `-0.0348` n `26`; metal avg `-0.0656` n `20`; unknown avg `110.0419` n `1134`
- 24h: commodity avg `0.5189` n `13`; crypto_alt avg `-0.8061` n `237`; crypto_major avg `-0.3174` n `8`; equity avg `1.2916` n `152`; fx avg `-0.0316` n `6`; index avg `0.0592` n `26`; metal avg `-0.1921` n `20`; unknown avg `199.754` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
