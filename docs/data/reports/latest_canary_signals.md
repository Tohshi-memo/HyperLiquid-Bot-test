# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T19:37:30.446159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `-0.0229` n `228`; crypto_major avg `0.078` n `8`; equity avg `0.0058` n `78`; fx avg `-0.0001` n `6`; index avg `0.0084` n `23`; metal avg `-0.001` n `18`; unknown avg `0.2615` n `702`
- 1h: commodity avg `0.1229` n `12`; crypto_alt avg `0.0555` n `228`; crypto_major avg `0.0815` n `8`; equity avg `0.0224` n `78`; fx avg `-0.0045` n `6`; index avg `0.0194` n `23`; metal avg `0.0073` n `18`; unknown avg `0.1435` n `694`
- 4h: commodity avg `0.2661` n `12`; crypto_alt avg `-0.0833` n `228`; crypto_major avg `0.072` n `8`; equity avg `-0.0723` n `78`; fx avg `-0.0858` n `6`; index avg `-0.0096` n `23`; metal avg `-0.069` n `18`; unknown avg `-0.0264` n `694`
- 24h: commodity avg `0.376` n `12`; crypto_alt avg `1.5532` n `228`; crypto_major avg `0.5213` n `8`; equity avg `0.3576` n `78`; fx avg `-0.0716` n `6`; index avg `0.0166` n `23`; metal avg `-0.0693` n `18`; unknown avg `0.2465` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
