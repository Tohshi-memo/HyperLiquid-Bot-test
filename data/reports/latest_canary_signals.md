# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T07:22:34.590533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1241` n `13`; crypto_alt avg `-0.1428` n `239`; crypto_major avg `-0.2184` n `8`; equity avg `-0.396` n `166`; fx avg `0.0216` n `6`; index avg `-0.0512` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0339` n `1262`
- 1h: commodity avg `0.1618` n `13`; crypto_alt avg `-0.1793` n `239`; crypto_major avg `-0.0728` n `8`; equity avg `0.0398` n `166`; fx avg `0.0195` n `6`; index avg `0.0105` n `27`; metal avg `0.039` n `20`; unknown avg `211.7163` n `1250`
- 4h: commodity avg `0.1096` n `13`; crypto_alt avg `1.4585` n `239`; crypto_major avg `1.068` n `8`; equity avg `0.1865` n `166`; fx avg `0.0348` n `6`; index avg `0.0103` n `27`; metal avg `-0.1544` n `20`; unknown avg `-0.0265` n `1204`
- 24h: commodity avg `-0.8402` n `13`; crypto_alt avg `0.4668` n `239`; crypto_major avg `-0.2154` n `8`; equity avg `4.0496` n `166`; fx avg `-0.2138` n `6`; index avg `0.6316` n `27`; metal avg `-0.3597` n `20`; unknown avg `687.8347` n `1034`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
