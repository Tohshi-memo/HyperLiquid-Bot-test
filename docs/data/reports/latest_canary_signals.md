# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T22:37:26.581764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0589` n `13`; crypto_alt avg `0.329` n `239`; crypto_major avg `0.4044` n `8`; equity avg `-0.0527` n `160`; fx avg `-0.0068` n `6`; index avg `-0.0059` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.0973` n `1259`
- 1h: commodity avg `-0.0168` n `13`; crypto_alt avg `0.1105` n `239`; crypto_major avg `0.4082` n `8`; equity avg `0.0005` n `160`; fx avg `-0.0041` n `6`; index avg `0.004` n `27`; metal avg `-0.003` n `20`; unknown avg `18.9804` n `1247`
- 4h: commodity avg `-0.3193` n `13`; crypto_alt avg `-0.0376` n `239`; crypto_major avg `0.5657` n `8`; equity avg `0.4192` n `160`; fx avg `-0.0126` n `6`; index avg `0.0821` n `27`; metal avg `0.2563` n `20`; unknown avg `-0.2239` n `1205`
- 24h: commodity avg `-0.5659` n `13`; crypto_alt avg `3.0215` n `239`; crypto_major avg `0.9993` n `8`; equity avg `5.2939` n `160`; fx avg `-0.124` n `6`; index avg `0.688` n `27`; metal avg `0.775` n `20`; unknown avg `5.567` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
