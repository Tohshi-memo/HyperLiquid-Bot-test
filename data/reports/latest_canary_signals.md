# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T21:17:27.606250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1408` n `228`; crypto_major avg `-0.1007` n `8`; equity avg `0.0668` n `67`; fx avg `0.0223` n `6`; index avg `0.0039` n `23`; metal avg `-0.0259` n `18`; unknown avg `0.2615` n `418`
- 1h: commodity avg `0.2981` n `12`; crypto_alt avg `-0.2496` n `228`; crypto_major avg `-0.2642` n `8`; equity avg `0.1352` n `67`; fx avg `0.007` n `6`; index avg `-0.0263` n `23`; metal avg `-0.0027` n `18`; unknown avg `0.3605` n `418`
- 4h: commodity avg `0.0286` n `12`; crypto_alt avg `-0.6387` n `228`; crypto_major avg `-0.7412` n `8`; equity avg `0.0257` n `67`; fx avg `0.03` n `6`; index avg `0.0984` n `23`; metal avg `0.3809` n `18`; unknown avg `-0.3696` n `418`
- 24h: commodity avg `1.0862` n `12`; crypto_alt avg `-1.9071` n `228`; crypto_major avg `-1.7178` n `8`; equity avg `-0.301` n `67`; fx avg `-0.1297` n `6`; index avg `0.3866` n `23`; metal avg `-0.8887` n `18`; unknown avg `0.1488` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
