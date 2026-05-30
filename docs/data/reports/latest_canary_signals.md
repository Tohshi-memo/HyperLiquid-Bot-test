# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T12:52:22.248562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0227` n `228`; crypto_major avg `-0.0034` n `8`; equity avg `0.0049` n `69`; fx avg `0.0015` n `6`; index avg `0.0142` n `23`; metal avg `-0.018` n `18`; unknown avg `-0.1822` n `421`
- 1h: commodity avg `0.1432` n `12`; crypto_alt avg `0.0082` n `228`; crypto_major avg `0.0122` n `8`; equity avg `0.1473` n `69`; fx avg `0.0169` n `6`; index avg `0.0271` n `23`; metal avg `-0.006` n `18`; unknown avg `0.2841` n `421`
- 4h: commodity avg `0.2034` n `12`; crypto_alt avg `0.0525` n `228`; crypto_major avg `0.3247` n `8`; equity avg `0.2314` n `69`; fx avg `0.0396` n `6`; index avg `-0.0037` n `23`; metal avg `0.0244` n `18`; unknown avg `0.1293` n `421`
- 24h: commodity avg `-0.2119` n `12`; crypto_alt avg `2.3512` n `228`; crypto_major avg `2.7049` n `8`; equity avg `1.5118` n `69`; fx avg `0.1128` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0143` n `18`; unknown avg `0.6329` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
