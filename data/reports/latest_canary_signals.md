# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T17:52:28.968996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.1905` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.7136` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.6768` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.115` n `228`; crypto_major avg `0.131` n `8`; equity avg `-0.0018` n `78`; fx avg `0.0279` n `6`; index avg `-0.0342` n `23`; metal avg `0.0027` n `18`; unknown avg `0.1093` n `687`
- 1h: commodity avg `-0.1318` n `12`; crypto_alt avg `0.2818` n `228`; crypto_major avg `0.2814` n `8`; equity avg `-0.0082` n `78`; fx avg `0.048` n `6`; index avg `-0.0512` n `23`; metal avg `0.0274` n `18`; unknown avg `0.1174` n `687`
- 4h: commodity avg `0.2508` n `12`; crypto_alt avg `-3.2354` n `228`; crypto_major avg `-4.4628` n `8`; equity avg `0.7277` n `78`; fx avg `-0.0669` n `6`; index avg `0.214` n `23`; metal avg `-4.2495` n `18`; unknown avg `-0.2482` n `572`
- 24h: commodity avg `0.2508` n `12`; crypto_alt avg `-3.2354` n `228`; crypto_major avg `-4.4628` n `8`; equity avg `0.7277` n `78`; fx avg `-0.0669` n `6`; index avg `0.214` n `23`; metal avg `-4.2495` n `18`; unknown avg `-0.2482` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
