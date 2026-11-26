# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T17:52:30.874878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `0.0011` n `239`; crypto_major avg `0.1532` n `8`; equity avg `-0.0068` n `168`; fx avg `-0.001` n `6`; index avg `0.0026` n `27`; metal avg `0.0121` n `20`; unknown avg `1.0909` n `1267`
- 1h: commodity avg `0.0315` n `13`; crypto_alt avg `0.1346` n `239`; crypto_major avg `0.1891` n `8`; equity avg `-0.0552` n `168`; fx avg `-0.0001` n `6`; index avg `0.0052` n `27`; metal avg `-0.0372` n `20`; unknown avg `0.7781` n `1261`
- 4h: commodity avg `0.0592` n `13`; crypto_alt avg `-0.2563` n `239`; crypto_major avg `-0.3982` n `8`; equity avg `-0.3536` n `168`; fx avg `-0.0223` n `6`; index avg `-0.0324` n `27`; metal avg `-0.0639` n `20`; unknown avg `1.7989` n `1243`
- 24h: commodity avg `0.032` n `13`; crypto_alt avg `2.4032` n `239`; crypto_major avg `1.8099` n `8`; equity avg `3.1451` n `168`; fx avg `-0.0122` n `6`; index avg `0.2481` n `27`; metal avg `0.7343` n `20`; unknown avg `14.8449` n `1055`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
