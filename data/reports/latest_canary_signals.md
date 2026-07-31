# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T09:52:26.115932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0792` n `12`; crypto_alt avg `0.019` n `230`; crypto_major avg `-0.0239` n `8`; equity avg `0.0139` n `102`; fx avg `0.0082` n `6`; index avg `-0.0036` n `25`; metal avg `0.0425` n `20`; unknown avg `-0.0899` n `780`
- 1h: commodity avg `0.2902` n `12`; crypto_alt avg `-0.2959` n `230`; crypto_major avg `-0.3452` n `8`; equity avg `-0.1283` n `102`; fx avg `0.0265` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0498` n `20`; unknown avg `-0.0875` n `780`
- 4h: commodity avg `0.4649` n `12`; crypto_alt avg `-0.2974` n `230`; crypto_major avg `-0.6895` n `8`; equity avg `-0.256` n `102`; fx avg `-0.0908` n `6`; index avg `-0.079` n `25`; metal avg `-0.1058` n `20`; unknown avg `-0.0813` n `747`
- 24h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.4194` n `230`; crypto_major avg `-0.3293` n `8`; equity avg `8.1076` n `102`; fx avg `-0.1727` n `6`; index avg `1.1857` n `25`; metal avg `0.1281` n `20`; unknown avg `0.0077` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
