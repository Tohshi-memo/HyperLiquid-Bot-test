# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T10:37:31.140605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0657` n `12`; crypto_alt avg `0.1622` n `229`; crypto_major avg `0.1891` n `8`; equity avg `0.3152` n `91`; fx avg `-0.0103` n `6`; index avg `0.0574` n `25`; metal avg `-0.0582` n `20`; unknown avg `0.0313` n `763`
- 1h: commodity avg `-0.162` n `12`; crypto_alt avg `0.0354` n `229`; crypto_major avg `0.0753` n `8`; equity avg `0.4795` n `91`; fx avg `-0.0122` n `6`; index avg `0.0733` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0621` n `763`
- 4h: commodity avg `0.3607` n `12`; crypto_alt avg `-0.8259` n `229`; crypto_major avg `-0.3718` n `8`; equity avg `-1.3551` n `91`; fx avg `0.047` n `6`; index avg `-0.3015` n `25`; metal avg `-1.155` n `20`; unknown avg `-0.2587` n `763`
- 24h: commodity avg `1.2496` n `12`; crypto_alt avg `-4.0214` n `229`; crypto_major avg `-3.0079` n `8`; equity avg `-2.8651` n `91`; fx avg `-0.1279` n `6`; index avg `-0.6507` n `25`; metal avg `-1.2858` n `20`; unknown avg `-0.8553` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
