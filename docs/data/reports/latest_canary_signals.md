# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:09:27.314493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0195` n `231`; crypto_major avg `0.092` n `8`; equity avg `-0.0069` n `122`; fx avg `-0.0079` n `6`; index avg `0.009` n `25`; metal avg `-0.009` n `20`; unknown avg `1.1056` n `793`
- 1h: commodity avg `0.0175` n `12`; crypto_alt avg `0.4244` n `231`; crypto_major avg `0.4586` n `8`; equity avg `0.0701` n `122`; fx avg `0.0017` n `6`; index avg `0.022` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0502` n `793`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `1.6257` n `231`; crypto_major avg `0.378` n `8`; equity avg `0.1717` n `122`; fx avg `-0.0037` n `6`; index avg `0.0426` n `25`; metal avg `0.0218` n `20`; unknown avg `1.1079` n `793`
- 24h: commodity avg `0.0215` n `12`; crypto_alt avg `2.1407` n `231`; crypto_major avg `1.1438` n `8`; equity avg `0.6705` n `122`; fx avg `0.0257` n `6`; index avg `0.0874` n `25`; metal avg `0.0824` n `20`; unknown avg `7.5474` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
