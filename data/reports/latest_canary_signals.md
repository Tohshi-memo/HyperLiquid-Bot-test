# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T23:37:24.623276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `13`; crypto_alt avg `-0.0629` n `239`; crypto_major avg `-0.003` n `8`; equity avg `0.0346` n `160`; fx avg `-0.0164` n `6`; index avg `-0.0195` n `27`; metal avg `-0.059` n `20`; unknown avg `-0.0912` n `1261`
- 1h: commodity avg `-0.0245` n `13`; crypto_alt avg `-0.6306` n `239`; crypto_major avg `-0.2491` n `8`; equity avg `0.0491` n `160`; fx avg `0.026` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0204` n `20`; unknown avg `-0.0546` n `1255`
- 4h: commodity avg `-0.1057` n `13`; crypto_alt avg `-0.7724` n `239`; crypto_major avg `0.3102` n `8`; equity avg `0.4387` n `160`; fx avg `0.0282` n `6`; index avg `0.0442` n `27`; metal avg `0.1353` n `20`; unknown avg `-0.3175` n `1205`
- 24h: commodity avg `-0.4367` n `13`; crypto_alt avg `1.2435` n `239`; crypto_major avg `-0.3512` n `8`; equity avg `4.8916` n `160`; fx avg `-0.0893` n `6`; index avg `0.6152` n `27`; metal avg `0.5857` n `20`; unknown avg `4.3229` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
