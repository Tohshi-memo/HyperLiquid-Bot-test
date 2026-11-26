# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T17:22:28.262454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0566` n `13`; crypto_alt avg `-0.2024` n `239`; crypto_major avg `-0.1365` n `8`; equity avg `-0.0568` n `168`; fx avg `-0.0009` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0272` n `20`; unknown avg `-0.0256` n `1265`
- 1h: commodity avg `-0.1225` n `13`; crypto_alt avg `-0.0766` n `239`; crypto_major avg `0.1165` n `8`; equity avg `-0.0638` n `168`; fx avg `-0.0121` n `6`; index avg `-0.0175` n `27`; metal avg `-0.0269` n `20`; unknown avg `0.1442` n `1261`
- 4h: commodity avg `0.0494` n `13`; crypto_alt avg `-0.3371` n `239`; crypto_major avg `-0.4511` n `8`; equity avg `-0.3242` n `168`; fx avg `-0.0091` n `6`; index avg `-0.049` n `27`; metal avg `-0.0183` n `20`; unknown avg `-0.2096` n `1245`
- 24h: commodity avg `-0.0263` n `13`; crypto_alt avg `2.7042` n `239`; crypto_major avg `2.2668` n `8`; equity avg `4.185` n `168`; fx avg `-0.0156` n `6`; index avg `0.345` n `27`; metal avg `0.7888` n `20`; unknown avg `14.5005` n `1054`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
