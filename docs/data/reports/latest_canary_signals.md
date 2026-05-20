# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T22:52:17.926232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3094` n `12`; crypto_alt avg `0.0454` n `228`; crypto_major avg `-0.0627` n `8`; equity avg `0.0083` n `66`; fx avg `0.0067` n `6`; index avg `0.0226` n `23`; metal avg `-0.0377` n `18`; unknown avg `0.0235` n `384`
- 1h: commodity avg `-0.28` n `12`; crypto_alt avg `-0.2834` n `228`; crypto_major avg `-0.0285` n `8`; equity avg `-0.2725` n `66`; fx avg `0.0154` n `6`; index avg `-0.1781` n `23`; metal avg `-0.1747` n `18`; unknown avg `-0.1223` n `384`
- 4h: commodity avg `0.1802` n `12`; crypto_alt avg `0.0127` n `228`; crypto_major avg `0.4629` n `8`; equity avg `-0.2144` n `66`; fx avg `-0.0478` n `6`; index avg `-0.1085` n `23`; metal avg `-0.3313` n `18`; unknown avg `-0.2794` n `384`
- 24h: commodity avg `-2.4122` n `12`; crypto_alt avg `2.9754` n `228`; crypto_major avg `2.3377` n `8`; equity avg `1.4321` n `66`; fx avg `-0.0628` n `6`; index avg `1.0308` n `23`; metal avg `1.324` n `18`; unknown avg `1.092` n `373`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
