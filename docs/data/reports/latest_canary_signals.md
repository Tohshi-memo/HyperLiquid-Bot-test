# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T06:52:31.779167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `0.1153` n `237`; crypto_major avg `0.053` n `8`; equity avg `-0.096` n `152`; fx avg `0.0059` n `6`; index avg `-0.0155` n `26`; metal avg `0.0014` n `20`; unknown avg `0.4974` n `1240`
- 1h: commodity avg `-0.0162` n `13`; crypto_alt avg `-0.5688` n `237`; crypto_major avg `-0.309` n `8`; equity avg `-0.5073` n `152`; fx avg `0.0086` n `6`; index avg `-0.1021` n `26`; metal avg `-0.0615` n `20`; unknown avg `0.1652` n `1212`
- 4h: commodity avg `0.0115` n `13`; crypto_alt avg `0.5497` n `237`; crypto_major avg `0.7331` n `8`; equity avg `0.2438` n `152`; fx avg `0.0234` n `6`; index avg `-0.0081` n `26`; metal avg `0.0238` n `20`; unknown avg `1.0718` n `1202`
- 24h: commodity avg `-0.6101` n `13`; crypto_alt avg `-0.4496` n `237`; crypto_major avg `-0.2368` n `8`; equity avg `-0.5391` n `152`; fx avg `0.0587` n `6`; index avg `-0.0579` n `26`; metal avg `0.123` n `20`; unknown avg `0.3528` n `987`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2533`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
