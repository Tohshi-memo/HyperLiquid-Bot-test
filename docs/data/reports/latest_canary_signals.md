# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T04:07:26.586853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `0.0907` n `228`; crypto_major avg `-0.0293` n `8`; equity avg `0.0163` n `78`; fx avg `-0.0003` n `6`; index avg `-0.0018` n `23`; metal avg `0.0187` n `18`; unknown avg `-0.1342` n `687`
- 1h: commodity avg `-0.014` n `12`; crypto_alt avg `0.2592` n `228`; crypto_major avg `0.1686` n `8`; equity avg `0.1256` n `78`; fx avg `-0.0198` n `6`; index avg `-0.0173` n `23`; metal avg `0.0329` n `18`; unknown avg `2.0361` n `687`
- 4h: commodity avg `0.063` n `12`; crypto_alt avg `-0.5039` n `228`; crypto_major avg `-0.2661` n `8`; equity avg `0.0691` n `78`; fx avg `-0.0028` n `6`; index avg `0.007` n `23`; metal avg `-0.0313` n `18`; unknown avg `-0.7694` n `679`
- 24h: commodity avg `0.435` n `12`; crypto_alt avg `-3.6837` n `228`; crypto_major avg `-4.4542` n `8`; equity avg `1.0672` n `78`; fx avg `-0.0947` n `6`; index avg `0.2888` n `23`; metal avg `-4.1401` n `18`; unknown avg `-0.4377` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0442`, n `668`, weak_sample_signal
