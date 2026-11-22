# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T19:30:01.071764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `-0.0589` n `239`; crypto_major avg `0.0313` n `8`; equity avg `0.0249` n `166`; fx avg `0.0` n `6`; index avg `-0.0021` n `27`; metal avg `0.0008` n `20`; unknown avg `3.655` n `1256`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `0.2669` n `239`; crypto_major avg `-0.1107` n `8`; equity avg `-0.0779` n `166`; fx avg `-0.0016` n `6`; index avg `-0.0275` n `27`; metal avg `-0.0383` n `20`; unknown avg `3.109` n `1252`
- 4h: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.1034` n `239`; crypto_major avg `-0.1027` n `8`; equity avg `0.1045` n `166`; fx avg `0.0192` n `6`; index avg `-0.007` n `27`; metal avg `-0.0325` n `20`; unknown avg `330.2729` n `1221`
- 24h: commodity avg `-0.1115` n `13`; crypto_alt avg `0.7324` n `239`; crypto_major avg `0.4086` n `8`; equity avg `0.8963` n `166`; fx avg `-0.0046` n `6`; index avg `0.1064` n `27`; metal avg `-0.04` n `20`; unknown avg `238.4085` n `1056`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
