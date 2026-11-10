# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T02:37:24.917038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `13`; crypto_alt avg `0.0232` n `239`; crypto_major avg `-0.0836` n `8`; equity avg `-0.0783` n `160`; fx avg `0.014` n `6`; index avg `-0.0207` n `27`; metal avg `-0.0615` n `20`; unknown avg `0.9047` n `1261`
- 1h: commodity avg `0.0261` n `13`; crypto_alt avg `-0.2085` n `239`; crypto_major avg `-0.3526` n `8`; equity avg `0.2378` n `160`; fx avg `0.018` n `6`; index avg `0.0203` n `27`; metal avg `-0.0714` n `20`; unknown avg `19.6865` n `1255`
- 4h: commodity avg `-0.0917` n `13`; crypto_alt avg `-0.8847` n `239`; crypto_major avg `-0.7589` n `8`; equity avg `-0.1642` n `160`; fx avg `0.0995` n `6`; index avg `-0.0941` n `27`; metal avg `-0.108` n `20`; unknown avg `0.4113` n `1247`
- 24h: commodity avg `-0.5379` n `13`; crypto_alt avg `-0.1085` n `239`; crypto_major avg `-1.1805` n `8`; equity avg `3.2532` n `160`; fx avg `0.0647` n `6`; index avg `0.3321` n `27`; metal avg `0.0178` n `20`; unknown avg `184.1168` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
