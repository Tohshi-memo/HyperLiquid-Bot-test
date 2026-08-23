# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T15:42:19.262704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.4048` n `231`; crypto_major avg `0.2403` n `8`; equity avg `0.012` n `122`; fx avg `0.0024` n `6`; index avg `-0.0139` n `25`; metal avg `0.0031` n `20`; unknown avg `0.059` n `793`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `1.4442` n `231`; crypto_major avg `0.5871` n `8`; equity avg `0.1605` n `122`; fx avg `0.008` n `6`; index avg `0.0099` n `25`; metal avg `0.0308` n `20`; unknown avg `0.3183` n `793`
- 4h: commodity avg `-0.0009` n `12`; crypto_alt avg `1.9196` n `231`; crypto_major avg `0.1134` n `8`; equity avg `0.179` n `122`; fx avg `0.0008` n `6`; index avg `0.0303` n `25`; metal avg `0.025` n `20`; unknown avg `2.865` n `793`
- 24h: commodity avg `0.0707` n `12`; crypto_alt avg `2.8715` n `231`; crypto_major avg `1.7697` n `8`; equity avg `0.6818` n `122`; fx avg `0.0495` n `6`; index avg `0.0674` n `25`; metal avg `0.0629` n `20`; unknown avg `8.1473` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
