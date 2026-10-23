# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T13:07:27.822103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0963` n `13`; crypto_alt avg `-0.0447` n `237`; crypto_major avg `-0.0169` n `8`; equity avg `0.1589` n `152`; fx avg `-0.0015` n `6`; index avg `0.0171` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.0898` n `1231`
- 1h: commodity avg `-0.1784` n `13`; crypto_alt avg `-0.0383` n `237`; crypto_major avg `-0.0385` n `8`; equity avg `-0.1377` n `152`; fx avg `0.0056` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0166` n `20`; unknown avg `1.2611` n `1231`
- 4h: commodity avg `-0.069` n `13`; crypto_alt avg `-0.2992` n `237`; crypto_major avg `-0.3719` n `8`; equity avg `-1.0559` n `152`; fx avg `-0.0207` n `6`; index avg `-0.1336` n `26`; metal avg `-0.025` n `20`; unknown avg `2.138` n `1213`
- 24h: commodity avg `0.0368` n `13`; crypto_alt avg `0.091` n `237`; crypto_major avg `0.2049` n `8`; equity avg `-1.5733` n `152`; fx avg `-0.0848` n `6`; index avg `-0.235` n `26`; metal avg `-0.4016` n `20`; unknown avg `50.0117` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
