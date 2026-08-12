# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T15:44:53.610238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6444` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `0.2037` n `8`; equity avg `-0.1123` n `113`; fx avg `0.0113` n `6`; index avg `-0.0232` n `25`; metal avg `-0.072` n `20`; unknown avg `-0.0252` n `786`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `0.0455` n `230`; crypto_major avg `0.2839` n `8`; equity avg `0.0658` n `113`; fx avg `0.005` n `6`; index avg `-0.054` n `25`; metal avg `-0.0876` n `20`; unknown avg `-0.0544` n `786`
- 4h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.399` n `230`; crypto_major avg `-0.5405` n `8`; equity avg `1.1039` n `113`; fx avg `0.0066` n `6`; index avg `0.0971` n `25`; metal avg `-0.196` n `20`; unknown avg `0.0121` n `786`
- 24h: commodity avg `0.1322` n `12`; crypto_alt avg `0.1774` n `230`; crypto_major avg `1.3384` n `8`; equity avg `3.1174` n `113`; fx avg `0.042` n `6`; index avg `0.3273` n `25`; metal avg `0.308` n `20`; unknown avg `0.0435` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
