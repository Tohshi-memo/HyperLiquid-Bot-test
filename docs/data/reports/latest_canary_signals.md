# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T22:52:17.891763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `-0.0211` n `228`; crypto_major avg `0.013` n `8`; equity avg `-0.0169` n `67`; fx avg `0.0013` n `6`; index avg `-0.0212` n `23`; metal avg `0.0449` n `18`; unknown avg `-0.0396` n `418`
- 1h: commodity avg `0.1113` n `12`; crypto_alt avg `-0.2161` n `228`; crypto_major avg `-0.1431` n `8`; equity avg `-0.0489` n `67`; fx avg `0.0231` n `6`; index avg `-0.0543` n `23`; metal avg `0.0704` n `18`; unknown avg `0.0903` n `418`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.2205` n `228`; crypto_major avg `-0.5982` n `8`; equity avg `0.0743` n `67`; fx avg `0.0393` n `6`; index avg `-0.0218` n `23`; metal avg `0.4` n `18`; unknown avg `-0.3127` n `418`
- 24h: commodity avg `0.8623` n `12`; crypto_alt avg `-1.5473` n `228`; crypto_major avg `-1.5147` n `8`; equity avg `-0.1894` n `67`; fx avg `-0.1168` n `6`; index avg `0.5303` n `23`; metal avg `-0.8491` n `18`; unknown avg `0.1129` n `395`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
