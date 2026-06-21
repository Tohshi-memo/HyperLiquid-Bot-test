# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T12:37:30.204805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.063` n `228`; crypto_major avg `0.0975` n `8`; equity avg `-0.0064` n `78`; fx avg `0.0546` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0176` n `18`; unknown avg `0.0184` n `702`
- 1h: commodity avg `0.2072` n `12`; crypto_alt avg `-0.0477` n `228`; crypto_major avg `-0.2572` n `8`; equity avg `-0.0452` n `78`; fx avg `0.0341` n `6`; index avg `-0.0081` n `23`; metal avg `-0.0263` n `18`; unknown avg `0.0843` n `702`
- 4h: commodity avg `0.1567` n `12`; crypto_alt avg `0.2573` n `228`; crypto_major avg `-0.0563` n `8`; equity avg `-0.0373` n `78`; fx avg `0.0381` n `6`; index avg `0.0023` n `23`; metal avg `-0.0631` n `18`; unknown avg `-0.1569` n `702`
- 24h: commodity avg `0.2971` n `12`; crypto_alt avg `1.3018` n `228`; crypto_major avg `-0.4491` n `8`; equity avg `0.3249` n `78`; fx avg `0.056` n `6`; index avg `0.021` n `23`; metal avg `-0.1043` n `18`; unknown avg `0.0412` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
