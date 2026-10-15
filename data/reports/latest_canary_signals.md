# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T21:22:44.014123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.3946` n `236`; crypto_major avg `0.2617` n `8`; equity avg `0.3068` n `151`; fx avg `-0.0032` n `6`; index avg `0.0243` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.2158` n `1136`
- 1h: commodity avg `-0.039` n `13`; crypto_alt avg `-0.0318` n `236`; crypto_major avg `-0.0681` n `8`; equity avg `-0.2332` n `151`; fx avg `-0.0219` n `6`; index avg `-0.0408` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.2812` n `1120`
- 4h: commodity avg `-0.0959` n `13`; crypto_alt avg `0.0025` n `236`; crypto_major avg `-0.1376` n `8`; equity avg `1.1255` n `151`; fx avg `-0.0168` n `6`; index avg `0.0798` n `26`; metal avg `0.1325` n `20`; unknown avg `-0.0402` n `1052`
- 24h: commodity avg `-0.2481` n `13`; crypto_alt avg `1.0315` n `236`; crypto_major avg `0.9029` n `8`; equity avg `0.253` n `151`; fx avg `0.1647` n `6`; index avg `-0.0922` n `26`; metal avg `0.5254` n `20`; unknown avg `23.5492` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0733`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0509`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `666`, weak_sample_signal
