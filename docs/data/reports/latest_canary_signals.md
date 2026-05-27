# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T04:45:36.995171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.196` n `228`; crypto_major avg `0.2628` n `8`; equity avg `0.0977` n `67`; fx avg `-0.005` n `6`; index avg `0.0333` n `23`; metal avg `0.1491` n `18`; unknown avg `0.2631` n `418`
- 1h: commodity avg `-0.1212` n `12`; crypto_alt avg `-0.4839` n `228`; crypto_major avg `-0.1233` n `8`; equity avg `-0.1562` n `67`; fx avg `-0.0124` n `6`; index avg `-0.0801` n `23`; metal avg `0.1425` n `18`; unknown avg `1.02` n `418`
- 4h: commodity avg `-0.5053` n `12`; crypto_alt avg `-1.555` n `228`; crypto_major avg `-0.5545` n `8`; equity avg `-0.2814` n `67`; fx avg `-0.0701` n `6`; index avg `-0.1397` n `23`; metal avg `-0.4111` n `18`; unknown avg `0.4876` n `418`
- 24h: commodity avg `-0.3301` n `12`; crypto_alt avg `-1.6188` n `228`; crypto_major avg `-0.7402` n `8`; equity avg `0.4653` n `67`; fx avg `-0.0776` n `6`; index avg `0.8139` n `23`; metal avg `0.0863` n `18`; unknown avg `1.3678` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
