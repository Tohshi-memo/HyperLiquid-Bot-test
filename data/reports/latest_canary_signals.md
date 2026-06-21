# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T22:07:27.116344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1965` n `12`; crypto_alt avg `-0.1405` n `228`; crypto_major avg `-0.2566` n `8`; equity avg `-0.1291` n `78`; fx avg `-0.0003` n `6`; index avg `-0.0421` n `23`; metal avg `-0.0083` n `18`; unknown avg `0.0222` n `702`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `0.3299` n `228`; crypto_major avg `0.2417` n `8`; equity avg `0.0557` n `78`; fx avg `0.0618` n `6`; index avg `-0.0703` n `23`; metal avg `-0.02` n `18`; unknown avg `0.1035` n `702`
- 4h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.9377` n `228`; crypto_major avg `-0.6521` n `8`; equity avg `-0.1771` n `78`; fx avg `-0.0575` n `6`; index avg `-0.0665` n `23`; metal avg `-0.0691` n `18`; unknown avg `0.7925` n `694`
- 24h: commodity avg `0.1993` n `12`; crypto_alt avg `0.0763` n `228`; crypto_major avg `-1.0168` n `8`; equity avg `0.0081` n `78`; fx avg `-0.1212` n `6`; index avg `-0.0566` n `23`; metal avg `-0.1806` n `18`; unknown avg `0.6314` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
