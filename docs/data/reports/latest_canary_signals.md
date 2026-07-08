# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T19:52:30.492702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `-0.1029` n `229`; crypto_major avg `-0.1214` n `8`; equity avg `0.0196` n `91`; fx avg `0.005` n `6`; index avg `0.0041` n `25`; metal avg `-0.0576` n `20`; unknown avg `-0.0773` n `764`
- 1h: commodity avg `0.0871` n `12`; crypto_alt avg `-0.1926` n `229`; crypto_major avg `-0.0241` n `8`; equity avg `0.2705` n `91`; fx avg `-0.0089` n `6`; index avg `0.0308` n `25`; metal avg `-0.0796` n `20`; unknown avg `1.2542` n `764`
- 4h: commodity avg `-0.5773` n `12`; crypto_alt avg `0.6453` n `229`; crypto_major avg `0.7249` n `8`; equity avg `1.5991` n `91`; fx avg `-0.0133` n `6`; index avg `0.3422` n `25`; metal avg `0.4734` n `20`; unknown avg `1.3975` n `764`
- 24h: commodity avg `0.4155` n `12`; crypto_alt avg `-2.4108` n `229`; crypto_major avg `-3.0172` n `8`; equity avg `1.0627` n `91`; fx avg `0.0082` n `6`; index avg `0.0014` n `25`; metal avg `-0.7822` n `20`; unknown avg `0.1052` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
