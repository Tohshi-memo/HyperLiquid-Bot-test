# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T20:07:19.204401+00:00`
- Correlation status: `ready`
- Asset price records: `580`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.5155` n `12`; crypto_alt avg `0.3742` n `228`; crypto_major avg `0.2583` n `8`; equity avg `0.6557` n `65`; fx avg `-0.0063` n `5`; index avg `0.0016` n `23`; metal avg `0.3254` n `18`; unknown avg `0.0506` n `365`
- 1h: commodity avg `-0.3245` n `12`; crypto_alt avg `0.6086` n `228`; crypto_major avg `0.2609` n `8`; equity avg `0.7825` n `65`; fx avg `0.0089` n `5`; index avg `0.093` n `23`; metal avg `0.2551` n `18`; unknown avg `-0.0732` n `365`
- 4h: commodity avg `0.3379` n `12`; crypto_alt avg `1.8717` n `228`; crypto_major avg `0.5055` n `8`; equity avg `0.2125` n `65`; fx avg `-0.0034` n `5`; index avg `-0.3316` n `23`; metal avg `-0.242` n `18`; unknown avg `0.2652` n `365`
- 24h: commodity avg `0.2048` n `12`; crypto_alt avg `1.5441` n `228`; crypto_major avg `-1.8677` n `8`; equity avg `-0.9236` n `65`; fx avg `0.1698` n `5`; index avg `-0.9526` n `23`; metal avg `0.3547` n `18`; unknown avg `-0.3247` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `576`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `576`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `576`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `576`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `572`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `572`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0941`, n `572`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0896`, n `572`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `572`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0801`, n `572`, weak_sample_signal
