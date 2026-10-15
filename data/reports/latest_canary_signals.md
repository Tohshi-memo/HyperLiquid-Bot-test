# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T02:07:30.073233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `13`; crypto_alt avg `-0.1428` n `236`; crypto_major avg `-0.0687` n `8`; equity avg `0.1579` n `151`; fx avg `0.0321` n `6`; index avg `0.0279` n `26`; metal avg `-0.064` n `20`; unknown avg `0.2152` n `1134`
- 1h: commodity avg `-0.0933` n `13`; crypto_alt avg `-0.3669` n `236`; crypto_major avg `-0.1962` n `8`; equity avg `0.0167` n `151`; fx avg `0.0388` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0508` n `20`; unknown avg `0.8581` n `1134`
- 4h: commodity avg `-0.2963` n `13`; crypto_alt avg `-0.8895` n `236`; crypto_major avg `-0.2537` n `8`; equity avg `-1.2327` n `151`; fx avg `0.2537` n `6`; index avg `-0.3547` n `26`; metal avg `0.1746` n `20`; unknown avg `0.7779` n `1128`
- 24h: commodity avg `-0.5271` n `13`; crypto_alt avg `-3.413` n `236`; crypto_major avg `-2.5919` n `8`; equity avg `-5.8961` n `151`; fx avg `0.1036` n `6`; index avg `-0.9951` n `26`; metal avg `-0.6816` n `20`; unknown avg `1394.3748` n `890`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1183`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0984`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0827`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0738`, n `666`, weak_sample_signal
