# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T00:22:17.488566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.0126` n `228`; crypto_major avg `-0.077` n `8`; equity avg `-0.246` n `67`; fx avg `-0.002` n `6`; index avg `-0.1102` n `23`; metal avg `-0.0217` n `18`; unknown avg `0.1364` n `418`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.0942` n `228`; crypto_major avg `0.0829` n `8`; equity avg `-0.0218` n `67`; fx avg `0.0043` n `6`; index avg `0.0399` n `23`; metal avg `0.2271` n `18`; unknown avg `-0.0153` n `418`
- 4h: commodity avg `-0.0559` n `12`; crypto_alt avg `-0.1147` n `228`; crypto_major avg `-0.0499` n `8`; equity avg `0.0716` n `67`; fx avg `0.0025` n `6`; index avg `0.0925` n `23`; metal avg `0.3053` n `18`; unknown avg `-0.2869` n `418`
- 24h: commodity avg `0.3628` n `12`; crypto_alt avg `-1.1368` n `228`; crypto_major avg `-1.0712` n `8`; equity avg `0.437` n `67`; fx avg `-0.0941` n `6`; index avg `0.9465` n `23`; metal avg `0.084` n `18`; unknown avg `0.234` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
