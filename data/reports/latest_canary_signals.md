# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T19:37:32.758196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `13`; crypto_alt avg `0.0002` n `237`; crypto_major avg `-0.0095` n `8`; equity avg `-0.0247` n `152`; fx avg `0.0051` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.776` n `1222`
- 1h: commodity avg `-0.0548` n `13`; crypto_alt avg `-0.198` n `237`; crypto_major avg `-0.043` n `8`; equity avg `0.0154` n `152`; fx avg `0.0214` n `6`; index avg `0.0056` n `26`; metal avg `-0.0106` n `20`; unknown avg `7.1692` n `1222`
- 4h: commodity avg `-0.0586` n `13`; crypto_alt avg `0.1909` n `237`; crypto_major avg `0.0493` n `8`; equity avg `0.276` n `152`; fx avg `0.0143` n `6`; index avg `0.0417` n `26`; metal avg `0.0372` n `20`; unknown avg `0.9972` n `1176`
- 24h: commodity avg `-0.2233` n `13`; crypto_alt avg `0.2864` n `237`; crypto_major avg `0.6839` n `8`; equity avg `0.6224` n `152`; fx avg `0.0554` n `6`; index avg `0.1294` n `26`; metal avg `0.1282` n `20`; unknown avg `10.0751` n `1029`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
