# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T23:43:41.633800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `0.0458` n `228`; crypto_major avg `-0.0681` n `8`; equity avg `-0.0106` n `67`; fx avg `-0.053` n `6`; index avg `-0.002` n `23`; metal avg `-0.4502` n `18`; unknown avg `0.0316` n `405`
- 1h: commodity avg `0.21` n `12`; crypto_alt avg `0.2601` n `228`; crypto_major avg `0.1293` n `8`; equity avg `-0.1394` n `67`; fx avg `-0.051` n `6`; index avg `-0.0934` n `23`; metal avg `-0.2897` n `18`; unknown avg `-0.1915` n `405`
- 4h: commodity avg `0.1163` n `12`; crypto_alt avg `-0.7419` n `228`; crypto_major avg `-0.4053` n `8`; equity avg `-0.2301` n `67`; fx avg `-0.0214` n `6`; index avg `-0.1579` n `23`; metal avg `-0.348` n `18`; unknown avg `-0.5847` n `405`
- 24h: commodity avg `-0.1998` n `12`; crypto_alt avg `1.5455` n `228`; crypto_major avg `-0.2109` n `8`; equity avg `0.5977` n `67`; fx avg `-0.1105` n `6`; index avg `0.4326` n `23`; metal avg `-0.2564` n `18`; unknown avg `0.7878` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
