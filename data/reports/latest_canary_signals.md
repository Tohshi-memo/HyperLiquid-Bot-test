# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T00:37:17.177473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.3751` n `228`; crypto_major avg `0.1685` n `8`; equity avg `0.1812` n `67`; fx avg `-0.0116` n `6`; index avg `0.0942` n `23`; metal avg `0.032` n `18`; unknown avg `1.7471` n `418`
- 1h: commodity avg `0.0401` n `12`; crypto_alt avg `0.3414` n `228`; crypto_major avg `0.2076` n `8`; equity avg `0.1239` n `67`; fx avg `-0.0056` n `6`; index avg `0.1301` n `23`; metal avg `0.1499` n `18`; unknown avg `1.0895` n `418`
- 4h: commodity avg `-0.0731` n `12`; crypto_alt avg `0.3895` n `228`; crypto_major avg `0.2026` n `8`; equity avg `0.2382` n `67`; fx avg `-0.0087` n `6`; index avg `0.1547` n `23`; metal avg `0.3281` n `18`; unknown avg `-0.144` n `418`
- 24h: commodity avg `0.4396` n `12`; crypto_alt avg `-0.504` n `228`; crypto_major avg `-0.6743` n `8`; equity avg `0.426` n `67`; fx avg `-0.0562` n `6`; index avg `0.9682` n `23`; metal avg `-0.1364` n `18`; unknown avg `1.7004` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
