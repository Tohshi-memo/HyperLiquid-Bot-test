# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T07:37:27.414947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0868` n `12`; crypto_alt avg `-0.1419` n `230`; crypto_major avg `-0.1671` n `8`; equity avg `-0.1535` n `102`; fx avg `0.0005` n `6`; index avg `-0.0339` n `25`; metal avg `-0.0551` n `20`; unknown avg `-0.0237` n `774`
- 1h: commodity avg `0.0305` n `12`; crypto_alt avg `-0.0916` n `230`; crypto_major avg `-0.1339` n `8`; equity avg `0.103` n `102`; fx avg `-0.0103` n `6`; index avg `0.0474` n `25`; metal avg `0.0297` n `20`; unknown avg `0.0028` n `774`
- 4h: commodity avg `-0.0912` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `-0.1358` n `8`; equity avg `-0.4306` n `102`; fx avg `-0.0286` n `6`; index avg `-0.0345` n `25`; metal avg `-0.024` n `20`; unknown avg `-0.0203` n `758`
- 24h: commodity avg `-0.5756` n `12`; crypto_alt avg `-3.7908` n `230`; crypto_major avg `-3.6787` n `8`; equity avg `-4.1309` n `102`; fx avg `-0.1611` n `6`; index avg `-0.8325` n `25`; metal avg `-0.4887` n `20`; unknown avg `1158.5392` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
