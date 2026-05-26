# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T07:07:16.013213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.282` n `12`; crypto_alt avg `-0.2614` n `228`; crypto_major avg `-0.1475` n `8`; equity avg `-0.0793` n `67`; fx avg `-0.0118` n `6`; index avg `0.0065` n `23`; metal avg `-0.0107` n `18`; unknown avg `0.0691` n `417`
- 1h: commodity avg `0.2188` n `12`; crypto_alt avg `-0.1922` n `228`; crypto_major avg `-0.1474` n `8`; equity avg `-0.0654` n `67`; fx avg `-0.0252` n `6`; index avg `0.0155` n `23`; metal avg `0.0336` n `18`; unknown avg `-0.0907` n `417`
- 4h: commodity avg `0.3167` n `12`; crypto_alt avg `0.943` n `228`; crypto_major avg `0.6958` n `8`; equity avg `0.0394` n `67`; fx avg `-0.0614` n `6`; index avg `0.0476` n `23`; metal avg `-0.0848` n `18`; unknown avg `0.3081` n `397`
- 24h: commodity avg `0.5498` n `12`; crypto_alt avg `-0.6397` n `228`; crypto_major avg `-1.1376` n `8`; equity avg `-0.5442` n `67`; fx avg `-0.1022` n `6`; index avg `-0.0749` n `23`; metal avg `-0.3872` n `18`; unknown avg `0.3389` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
