# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T11:52:24.400876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0824` n `230`; crypto_major avg `-0.0454` n `8`; equity avg `-0.0599` n `112`; fx avg `-0.0017` n `6`; index avg `-0.006` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.01` n `782`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `0.092` n `230`; crypto_major avg `0.0219` n `8`; equity avg `0.125` n `112`; fx avg `0.0137` n `6`; index avg `0.0281` n `25`; metal avg `-0.1005` n `20`; unknown avg `0.0067` n `782`
- 4h: commodity avg `-0.3738` n `12`; crypto_alt avg `0.1062` n `230`; crypto_major avg `0.7269` n `8`; equity avg `0.526` n `112`; fx avg `-0.029` n `6`; index avg `0.0715` n `25`; metal avg `0.0242` n `20`; unknown avg `0.1792` n `782`
- 24h: commodity avg `0.1511` n `12`; crypto_alt avg `0.4211` n `230`; crypto_major avg `0.2232` n `8`; equity avg `2.0835` n `109`; fx avg `-0.0818` n `6`; index avg `0.1215` n `25`; metal avg `0.2484` n `20`; unknown avg `0.3364` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
