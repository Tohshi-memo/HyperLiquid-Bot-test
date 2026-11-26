# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T04:52:29.626376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `-0.1465` n `239`; crypto_major avg `-0.0411` n `8`; equity avg `-0.072` n `168`; fx avg `-0.0018` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0342` n `20`; unknown avg `157.8423` n `1267`
- 1h: commodity avg `0.0082` n `13`; crypto_alt avg `-0.1513` n `239`; crypto_major avg `0.0286` n `8`; equity avg `0.259` n `168`; fx avg `-0.0113` n `6`; index avg `0.0375` n `27`; metal avg `0.0816` n `20`; unknown avg `0.1816` n `1249`
- 4h: commodity avg `0.1312` n `13`; crypto_alt avg `0.2309` n `239`; crypto_major avg `0.7226` n `8`; equity avg `0.2119` n `168`; fx avg `-0.042` n `6`; index avg `0.0122` n `27`; metal avg `0.3445` n `20`; unknown avg `35.1492` n `1245`
- 24h: commodity avg `0.7378` n `13`; crypto_alt avg `3.4487` n `239`; crypto_major avg `3.4023` n `8`; equity avg `2.772` n `168`; fx avg `0.0115` n `6`; index avg `0.2135` n `27`; metal avg `0.6584` n `20`; unknown avg `773.1217` n `1019`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
