# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T21:22:25.789006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2053` n `12`; crypto_alt avg `-0.0697` n `228`; crypto_major avg `0.0963` n `8`; equity avg `-0.2992` n `73`; fx avg `-0.0274` n `6`; index avg `-0.0658` n `23`; metal avg `0.1106` n `18`; unknown avg `-0.1083` n `419`
- 1h: commodity avg `0.127` n `12`; crypto_alt avg `-0.2089` n `228`; crypto_major avg `0.0454` n `8`; equity avg `-0.8779` n `73`; fx avg `-0.038` n `6`; index avg `-0.1917` n `23`; metal avg `-0.0021` n `18`; unknown avg `0.3337` n `419`
- 4h: commodity avg `0.0889` n `12`; crypto_alt avg `-0.5157` n `228`; crypto_major avg `-0.2224` n `8`; equity avg `-0.9949` n `73`; fx avg `-0.0074` n `6`; index avg `-0.2494` n `23`; metal avg `-0.3856` n `18`; unknown avg `-0.2664` n `419`
- 24h: commodity avg `-0.6116` n `12`; crypto_alt avg `-0.0935` n `228`; crypto_major avg `-2.0312` n `8`; equity avg `-3.4106` n `72`; fx avg `0.0365` n `6`; index avg `-0.7489` n `23`; metal avg `-2.224` n `18`; unknown avg `-0.0581` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
