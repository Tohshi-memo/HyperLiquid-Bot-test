# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T06:37:19.503372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.1659` n `228`; crypto_major avg `0.1365` n `8`; equity avg `0.0059` n `67`; fx avg `0.0085` n `6`; index avg `0.0038` n `23`; metal avg `-0.0116` n `18`; unknown avg `0.2056` n `417`
- 1h: commodity avg `-0.0571` n `12`; crypto_alt avg `-0.2295` n `228`; crypto_major avg `-0.0592` n `8`; equity avg `0.0576` n `67`; fx avg `-0.0056` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0791` n `18`; unknown avg `-0.0583` n `397`
- 4h: commodity avg `0.0926` n `12`; crypto_alt avg `0.8503` n `228`; crypto_major avg `0.6185` n `8`; equity avg `0.111` n `67`; fx avg `-0.0555` n `6`; index avg `0.0275` n `23`; metal avg `-0.1447` n `18`; unknown avg `-0.0155` n `397`
- 24h: commodity avg `0.3019` n `12`; crypto_alt avg `-0.3821` n `228`; crypto_major avg `-0.9424` n `8`; equity avg `-0.3654` n `67`; fx avg `-0.0755` n `6`; index avg `-0.0244` n `23`; metal avg `-0.1539` n `18`; unknown avg `0.2225` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
