# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T07:22:21.268711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1396` n `12`; crypto_alt avg `-0.3369` n `228`; crypto_major avg `-0.3303` n `8`; equity avg `-0.1582` n `67`; fx avg `0.002` n `6`; index avg `-0.0529` n `23`; metal avg `-0.181` n `18`; unknown avg `0.0531` n `417`
- 1h: commodity avg `0.3737` n `12`; crypto_alt avg `-0.2866` n `228`; crypto_major avg `-0.3664` n `8`; equity avg `-0.2452` n `67`; fx avg `-0.0183` n `6`; index avg `-0.0539` n `23`; metal avg `-0.2418` n `18`; unknown avg `0.2861` n `417`
- 4h: commodity avg `0.4757` n `12`; crypto_alt avg `0.5542` n `228`; crypto_major avg `0.2699` n `8`; equity avg `-0.1763` n `67`; fx avg `-0.0475` n `6`; index avg `-0.0088` n `23`; metal avg `-0.4724` n `18`; unknown avg `0.2349` n `397`
- 24h: commodity avg `0.3399` n `12`; crypto_alt avg `-0.7195` n `228`; crypto_major avg `-1.2563` n `8`; equity avg `-0.6267` n `67`; fx avg `-0.1233` n `6`; index avg `-0.0324` n `23`; metal avg `-0.3432` n `18`; unknown avg `0.3025` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
