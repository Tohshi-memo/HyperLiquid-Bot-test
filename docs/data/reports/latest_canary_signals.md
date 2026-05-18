# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T20:52:22.464795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1123` n `12`; crypto_alt avg `-0.4763` n `228`; crypto_major avg `-0.326` n `8`; equity avg `-0.0275` n `66`; fx avg `-0.0179` n `6`; index avg `0.0044` n `23`; metal avg `0.063` n `18`; unknown avg `0.0996` n `383`
- 1h: commodity avg `0.158` n `12`; crypto_alt avg `-0.4304` n `228`; crypto_major avg `-0.5013` n `8`; equity avg `-0.0658` n `66`; fx avg `0.0044` n `6`; index avg `-0.0269` n `23`; metal avg `0.1309` n `18`; unknown avg `0.0215` n `383`
- 4h: commodity avg `-0.3009` n `12`; crypto_alt avg `0.5768` n `228`; crypto_major avg `0.573` n `8`; equity avg `0.2465` n `66`; fx avg `-0.0738` n `6`; index avg `0.1145` n `23`; metal avg `0.361` n `18`; unknown avg `0.3527` n `383`
- 24h: commodity avg `0.7972` n `12`; crypto_alt avg `-2.1444` n `228`; crypto_major avg `-2.411` n `8`; equity avg `-0.9911` n `66`; fx avg `0.1703` n `6`; index avg `-0.4331` n `23`; metal avg `1.0692` n `18`; unknown avg `-0.1099` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
