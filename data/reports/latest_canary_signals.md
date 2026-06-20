# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T14:37:32.454317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `0.2786` n `228`; crypto_major avg `0.2027` n `8`; equity avg `0.0516` n `78`; fx avg `0.0` n `6`; index avg `0.004` n `23`; metal avg `0.0087` n `18`; unknown avg `0.1103` n `701`
- 1h: commodity avg `0.0858` n `12`; crypto_alt avg `-0.1362` n `228`; crypto_major avg `-0.1688` n `8`; equity avg `-0.0138` n `78`; fx avg `0.0274` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0317` n `18`; unknown avg `-0.2485` n `701`
- 4h: commodity avg `0.2271` n `12`; crypto_alt avg `-0.8041` n `228`; crypto_major avg `-0.7728` n `8`; equity avg `-0.2588` n `78`; fx avg `0.0232` n `6`; index avg `-0.0112` n `23`; metal avg `-0.0542` n `18`; unknown avg `-0.2296` n `573`
- 24h: commodity avg `0.7405` n `12`; crypto_alt avg `-3.8509` n `228`; crypto_major avg `-4.1448` n `8`; equity avg `0.8951` n `78`; fx avg `-0.0579` n `6`; index avg `0.2702` n `23`; metal avg `-4.1551` n `18`; unknown avg `-0.3597` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
