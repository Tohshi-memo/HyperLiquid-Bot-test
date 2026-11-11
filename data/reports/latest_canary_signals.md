# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T01:22:27.518243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6448` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0605` n `13`; crypto_alt avg `0.1123` n `239`; crypto_major avg `0.127` n `8`; equity avg `0.382` n `161`; fx avg `0.0096` n `6`; index avg `0.039` n `27`; metal avg `0.0869` n `20`; unknown avg `0.3927` n `1261`
- 1h: commodity avg `-0.0159` n `13`; crypto_alt avg `-0.0941` n `239`; crypto_major avg `-0.2138` n `8`; equity avg `0.9338` n `161`; fx avg `0.0101` n `6`; index avg `0.0998` n `27`; metal avg `0.0564` n `20`; unknown avg `0.2455` n `1255`
- 4h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.5035` n `239`; crypto_major avg `-0.2805` n `8`; equity avg `1.3643` n `161`; fx avg `-0.0207` n `6`; index avg `0.1497` n `27`; metal avg `0.1142` n `20`; unknown avg `1.539` n `1243`
- 24h: commodity avg `0.0955` n `13`; crypto_alt avg `-0.534` n `239`; crypto_major avg `-2.8459` n `8`; equity avg `0.3462` n `161`; fx avg `-0.1804` n `6`; index avg `0.0702` n `27`; metal avg `-0.5598` n `20`; unknown avg `21.0513` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2732`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
