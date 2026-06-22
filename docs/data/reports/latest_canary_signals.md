# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T05:07:26.657768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `0.1856` n `8`; equity avg `0.1299` n `79`; fx avg `-0.0058` n `6`; index avg `0.0207` n `23`; metal avg `0.0274` n `18`; unknown avg `-0.3854` n `701`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.1626` n `228`; crypto_major avg `0.3735` n `8`; equity avg `0.0142` n `79`; fx avg `0.0036` n `6`; index avg `-0.0312` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.4669` n `701`
- 4h: commodity avg `-0.2191` n `12`; crypto_alt avg `0.1053` n `228`; crypto_major avg `-0.0064` n `8`; equity avg `0.0992` n `79`; fx avg `0.0248` n `6`; index avg `-0.0489` n `23`; metal avg `-0.5191` n `18`; unknown avg `-0.758` n `693`
- 24h: commodity avg `-0.3722` n `12`; crypto_alt avg `0.2566` n `228`; crypto_major avg `-0.4878` n `8`; equity avg `-0.5043` n `79`; fx avg `-0.0004` n `6`; index avg `-0.0407` n `23`; metal avg `0.1531` n `18`; unknown avg `-0.424` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
