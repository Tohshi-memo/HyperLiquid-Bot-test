# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T19:52:25.154797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0423` n `12`; crypto_alt avg `-0.0389` n `232`; crypto_major avg `-0.095` n `8`; equity avg `-0.0131` n `134`; fx avg `-0.0072` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.7047` n `794`
- 1h: commodity avg `0.0534` n `12`; crypto_alt avg `-0.0004` n `232`; crypto_major avg `-0.3396` n `8`; equity avg `-0.0394` n `134`; fx avg `-0.0177` n `6`; index avg `0.0165` n `26`; metal avg `-0.0091` n `20`; unknown avg `2.3077` n `792`
- 4h: commodity avg `0.0588` n `12`; crypto_alt avg `0.5619` n `232`; crypto_major avg `0.7111` n `8`; equity avg `0.0415` n `134`; fx avg `-0.0377` n `6`; index avg `0.0445` n `26`; metal avg `0.0191` n `20`; unknown avg `1.1086` n `786`
- 24h: commodity avg `0.128` n `12`; crypto_alt avg `2.5056` n `232`; crypto_major avg `2.376` n `8`; equity avg `0.1944` n `134`; fx avg `-0.0515` n `6`; index avg `0.0273` n `26`; metal avg `0.0348` n `20`; unknown avg `0.1995` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
