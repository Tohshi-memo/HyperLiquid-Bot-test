# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T14:52:40.311985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `13`; crypto_alt avg `-0.2912` n `239`; crypto_major avg `-0.2832` n `8`; equity avg `-0.023` n `168`; fx avg `-0.0169` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0177` n `20`; unknown avg `0.1475` n `1265`
- 1h: commodity avg `0.0576` n `13`; crypto_alt avg `-0.3505` n `239`; crypto_major avg `-0.3444` n `8`; equity avg `-0.1804` n `168`; fx avg `-0.0177` n `6`; index avg `-0.0247` n `27`; metal avg `0.03` n `20`; unknown avg `115.513` n `1261`
- 4h: commodity avg `0.1402` n `13`; crypto_alt avg `0.0837` n `239`; crypto_major avg `0.3045` n `8`; equity avg `0.4403` n `168`; fx avg `-0.0177` n `6`; index avg `0.0467` n `27`; metal avg `0.11` n `20`; unknown avg `2.3701` n `1253`
- 24h: commodity avg `0.2082` n `13`; crypto_alt avg `5.6213` n `239`; crypto_major avg `5.3213` n `8`; equity avg `6.6263` n `168`; fx avg `0.0731` n `6`; index avg `0.6243` n `27`; metal avg `1.3671` n `20`; unknown avg `3.4505` n `1059`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
