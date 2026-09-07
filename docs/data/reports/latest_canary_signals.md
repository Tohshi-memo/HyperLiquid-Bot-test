# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T12:22:25.925947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.1166` n `232`; crypto_major avg `0.0889` n `8`; equity avg `-0.0276` n `134`; fx avg `-0.0033` n `6`; index avg `-0.0132` n `26`; metal avg `0.0024` n `20`; unknown avg `6545.7165` n `764`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.3117` n `232`; crypto_major avg `0.2582` n `8`; equity avg `-0.0086` n `134`; fx avg `0.0048` n `6`; index avg `-0.0086` n `26`; metal avg `-0.008` n `20`; unknown avg `6631.7073` n `754`
- 4h: commodity avg `0.3029` n `12`; crypto_alt avg `0.9207` n `232`; crypto_major avg `0.4771` n `8`; equity avg `-0.0958` n `134`; fx avg `0.0777` n `6`; index avg `-0.0638` n `26`; metal avg `-0.2075` n `20`; unknown avg `6721.2944` n `744`
- 24h: commodity avg `0.1578` n `12`; crypto_alt avg `0.2801` n `232`; crypto_major avg `-0.7261` n `8`; equity avg `0.1277` n `134`; fx avg `-0.069` n `6`; index avg `-0.0264` n `26`; metal avg `-0.186` n `20`; unknown avg `2.2396` n `616`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
