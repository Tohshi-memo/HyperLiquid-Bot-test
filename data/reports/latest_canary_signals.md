# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T07:52:30.931090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `13`; crypto_alt avg `0.0871` n `237`; crypto_major avg `0.1538` n `8`; equity avg `-0.0983` n `152`; fx avg `-0.0042` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0164` n `20`; unknown avg `4.3722` n `1236`
- 1h: commodity avg `0.1176` n `13`; crypto_alt avg `-0.3166` n `237`; crypto_major avg `-0.1316` n `8`; equity avg `-0.0415` n `152`; fx avg `-0.0203` n `6`; index avg `0.0248` n `26`; metal avg `0.0129` n `20`; unknown avg `4.177` n `1232`
- 4h: commodity avg `0.1592` n `13`; crypto_alt avg `0.4245` n `237`; crypto_major avg `0.7354` n `8`; equity avg `0.0356` n `152`; fx avg `-0.0056` n `6`; index avg `-0.0391` n `26`; metal avg `-0.0652` n `20`; unknown avg `4.4948` n `1194`
- 24h: commodity avg `-0.4532` n `13`; crypto_alt avg `-1.0038` n `237`; crypto_major avg `-0.7394` n `8`; equity avg `-0.6986` n `152`; fx avg `0.0334` n `6`; index avg `-0.0528` n `26`; metal avg `0.0993` n `20`; unknown avg `0.524` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2533`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
