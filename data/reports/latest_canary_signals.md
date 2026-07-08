# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T09:07:30.482584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0939` n `12`; crypto_alt avg `-0.3574` n `229`; crypto_major avg `-0.2675` n `8`; equity avg `-0.4318` n `91`; fx avg `-0.013` n `6`; index avg `-0.1272` n `25`; metal avg `-0.1823` n `20`; unknown avg `-0.0238` n `763`
- 1h: commodity avg `0.6609` n `12`; crypto_alt avg `-1.1174` n `229`; crypto_major avg `-1.0202` n `8`; equity avg `-1.8959` n `91`; fx avg `0.0311` n `6`; index avg `-0.3943` n `25`; metal avg `-0.9252` n `20`; unknown avg `0.1273` n `763`
- 4h: commodity avg `0.653` n `12`; crypto_alt avg `-1.3674` n `229`; crypto_major avg `-1.2664` n `8`; equity avg `-2.2129` n `91`; fx avg `0.0144` n `6`; index avg `-0.5265` n `25`; metal avg `-1.1358` n `20`; unknown avg `-0.4226` n `743`
- 24h: commodity avg `1.3546` n `12`; crypto_alt avg `-3.7011` n `229`; crypto_major avg `-3.2391` n `8`; equity avg `-3.4231` n `91`; fx avg `-0.1451` n `6`; index avg `-0.753` n `25`; metal avg `-1.1039` n `20`; unknown avg `-0.7165` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
