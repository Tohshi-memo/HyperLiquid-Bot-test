# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T11:37:17.823842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `0.2248` n `8`; equity avg `0.0134` n `67`; fx avg `0.0186` n `6`; index avg `0.0106` n `23`; metal avg `-0.0069` n `18`; unknown avg `-0.1654` n `397`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0338` n `228`; crypto_major avg `0.0565` n `8`; equity avg `0.0705` n `67`; fx avg `0.0389` n `6`; index avg `0.0318` n `23`; metal avg `0.0249` n `18`; unknown avg `-0.0624` n `397`
- 4h: commodity avg `-0.275` n `12`; crypto_alt avg `0.617` n `228`; crypto_major avg `0.4438` n `8`; equity avg `0.331` n `67`; fx avg `0.0504` n `6`; index avg `0.0832` n `23`; metal avg `0.3498` n `18`; unknown avg `0.1018` n `397`
- 24h: commodity avg `-0.173` n `12`; crypto_alt avg `0.6648` n `228`; crypto_major avg `-0.1427` n `8`; equity avg `0.5638` n `67`; fx avg `0.039` n `6`; index avg `0.0618` n `23`; metal avg `0.766` n `18`; unknown avg `0.8543` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
