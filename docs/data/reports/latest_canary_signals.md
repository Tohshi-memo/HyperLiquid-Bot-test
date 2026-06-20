# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T16:22:31.171510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.0756` n `228`; crypto_major avg `-0.0668` n `8`; equity avg `0.0374` n `78`; fx avg `0.0` n `6`; index avg `0.0163` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.0393` n `701`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.2275` n `228`; crypto_major avg `-0.3728` n `8`; equity avg `-0.074` n `78`; fx avg `0.0385` n `6`; index avg `0.0031` n `23`; metal avg `-0.0362` n `18`; unknown avg `0.0304` n `701`
- 4h: commodity avg `0.1843` n `12`; crypto_alt avg `0.1312` n `228`; crypto_major avg `-0.0981` n `8`; equity avg `0.0069` n `78`; fx avg `0.0309` n `6`; index avg `-0.0023` n `23`; metal avg `0.0141` n `18`; unknown avg `-0.0495` n `701`
- 24h: commodity avg `0.1699` n `12`; crypto_alt avg `0.3694` n `228`; crypto_major avg `1.0996` n `8`; equity avg `0.3235` n `78`; fx avg `0.0766` n `6`; index avg `0.0242` n `23`; metal avg `0.3568` n `18`; unknown avg `-0.2764` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
