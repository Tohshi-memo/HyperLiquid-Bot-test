# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T18:22:39.564075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1384` n `12`; crypto_alt avg `-0.3063` n `228`; crypto_major avg `-0.4517` n `8`; equity avg `-0.0624` n `77`; fx avg `0.0034` n `6`; index avg `-0.0552` n `23`; metal avg `-0.0312` n `18`; unknown avg `0.03` n `687`
- 1h: commodity avg `0.0899` n `12`; crypto_alt avg `0.8188` n `228`; crypto_major avg `0.6921` n `8`; equity avg `0.2954` n `77`; fx avg `-0.0019` n `6`; index avg `0.1109` n `23`; metal avg `0.2941` n `18`; unknown avg `0.3948` n `687`
- 4h: commodity avg `-0.4196` n `12`; crypto_alt avg `0.7313` n `228`; crypto_major avg `0.2468` n `8`; equity avg `0.0425` n `77`; fx avg `0.0737` n `6`; index avg `-0.3602` n `23`; metal avg `0.2158` n `18`; unknown avg `0.6193` n `687`
- 24h: commodity avg `-0.9886` n `12`; crypto_alt avg `-1.0936` n `228`; crypto_major avg `-0.7843` n `8`; equity avg `-0.8592` n `77`; fx avg `-0.0087` n `6`; index avg `-0.6657` n `23`; metal avg `0.517` n `18`; unknown avg `0.9158` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
