# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T07:38:40.590074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0825` n `234`; crypto_major avg `-0.0479` n `8`; equity avg `0.0512` n `140`; fx avg `0.0306` n `6`; index avg `0.0087` n `26`; metal avg `0.0657` n `20`; unknown avg `-0.166` n `927`
- 1h: commodity avg `-0.0515` n `12`; crypto_alt avg `0.3845` n `234`; crypto_major avg `0.2841` n `8`; equity avg `0.1259` n `140`; fx avg `0.0092` n `6`; index avg `0.0296` n `26`; metal avg `0.1351` n `20`; unknown avg `-0.0378` n `925`
- 4h: commodity avg `-0.2578` n `12`; crypto_alt avg `0.5064` n `234`; crypto_major avg `0.8108` n `8`; equity avg `0.6897` n `140`; fx avg `0.0016` n `6`; index avg `0.1264` n `26`; metal avg `0.3975` n `20`; unknown avg `-0.0768` n `863`
- 24h: commodity avg `-0.3654` n `12`; crypto_alt avg `5.1145` n `234`; crypto_major avg `3.7769` n `8`; equity avg `2.211` n `140`; fx avg `0.1582` n `6`; index avg `0.3191` n `26`; metal avg `0.6023` n `20`; unknown avg `2.7392` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
