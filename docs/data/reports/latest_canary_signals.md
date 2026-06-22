# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T04:52:29.398915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.1293` n `228`; crypto_major avg `0.1209` n `8`; equity avg `0.0491` n `79`; fx avg `0.0016` n `6`; index avg `0.0138` n `23`; metal avg `0.0367` n `18`; unknown avg `-0.0074` n `701`
- 1h: commodity avg `-0.0258` n `12`; crypto_alt avg `0.043` n `228`; crypto_major avg `0.1111` n `8`; equity avg `-0.1809` n `79`; fx avg `-0.0108` n `6`; index avg `-0.0663` n `23`; metal avg `0.032` n `18`; unknown avg `-0.0983` n `701`
- 4h: commodity avg `-0.4366` n `12`; crypto_alt avg `0.0893` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `0.0861` n `79`; fx avg `0.0807` n `6`; index avg `-0.0288` n `23`; metal avg `-0.166` n `18`; unknown avg `-0.0103` n `685`
- 24h: commodity avg `-0.3559` n `12`; crypto_alt avg `0.1335` n `228`; crypto_major avg `-0.8081` n `8`; equity avg `-0.6069` n `79`; fx avg `0.0084` n `6`; index avg `-0.0458` n `23`; metal avg `0.1197` n `18`; unknown avg `-0.3523` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
