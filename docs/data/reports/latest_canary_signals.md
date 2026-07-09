# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T10:01:12.598730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1047` n `12`; crypto_alt avg `0.1598` n `229`; crypto_major avg `0.1437` n `8`; equity avg `-0.0152` n `91`; fx avg `-0.0051` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0778` n `764`
- 1h: commodity avg `0.1388` n `12`; crypto_alt avg `0.0746` n `229`; crypto_major avg `0.0551` n `8`; equity avg `0.0161` n `91`; fx avg `0.0019` n `6`; index avg `-0.0191` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.0438` n `764`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.2119` n `229`; crypto_major avg `0.0709` n `8`; equity avg `0.5035` n `91`; fx avg `0.0805` n `6`; index avg `0.0398` n `25`; metal avg `0.3516` n `20`; unknown avg `0.0783` n `764`
- 24h: commodity avg `-0.5411` n `12`; crypto_alt avg `2.1848` n `229`; crypto_major avg `1.2251` n `8`; equity avg `3.8738` n `91`; fx avg `0.1556` n `6`; index avg `0.5951` n `25`; metal avg `0.7359` n `20`; unknown avg `0.9178` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0656`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0578`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0557`, n `670`, weak_sample_signal
