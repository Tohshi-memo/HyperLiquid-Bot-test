# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T10:22:29.808855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `0.0168` n `232`; crypto_major avg `-0.0424` n `8`; equity avg `-0.0419` n `134`; fx avg `-0.0011` n `6`; index avg `0.0199` n `26`; metal avg `0.0063` n `20`; unknown avg `0.6433` n `792`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `0.0285` n `232`; crypto_major avg `-0.1379` n `8`; equity avg `0.0292` n `134`; fx avg `-0.0121` n `6`; index avg `0.0298` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.5707` n `790`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `0.5324` n `232`; crypto_major avg `0.8314` n `8`; equity avg `0.0349` n `134`; fx avg `-0.0101` n `6`; index avg `0.0039` n `26`; metal avg `-0.0038` n `20`; unknown avg `1.3435` n `778`
- 24h: commodity avg `0.1228` n `12`; crypto_alt avg `0.9693` n `232`; crypto_major avg `-0.9338` n `8`; equity avg `0.878` n `134`; fx avg `-0.1122` n `6`; index avg `0.0783` n `26`; metal avg `-0.1056` n `20`; unknown avg `16.4822` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
