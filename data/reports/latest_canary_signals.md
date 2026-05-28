# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T16:37:20.599554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1191` n `12`; crypto_alt avg `-0.0522` n `228`; crypto_major avg `0.0444` n `8`; equity avg `-0.1003` n `67`; fx avg `-0.0082` n `6`; index avg `0.024` n `23`; metal avg `-0.0823` n `18`; unknown avg `-0.1936` n `419`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `0.5893` n `228`; crypto_major avg `0.7684` n `8`; equity avg `0.061` n `67`; fx avg `-0.0027` n `6`; index avg `0.089` n `23`; metal avg `0.4612` n `18`; unknown avg `0.1432` n `419`
- 4h: commodity avg `0.3806` n `12`; crypto_alt avg `0.8008` n `228`; crypto_major avg `1.2445` n `8`; equity avg `1.7583` n `67`; fx avg `0.0081` n `6`; index avg `1.2193` n `23`; metal avg `1.7782` n `18`; unknown avg `0.059` n `419`
- 24h: commodity avg `0.4586` n `12`; crypto_alt avg `-4.7016` n `228`; crypto_major avg `-1.9771` n `8`; equity avg `1.2288` n `67`; fx avg `0.0019` n `6`; index avg `0.9908` n `23`; metal avg `0.5217` n `18`; unknown avg `-1.1382` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
