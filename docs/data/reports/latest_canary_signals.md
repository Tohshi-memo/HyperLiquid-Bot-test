# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T09:42:13.031420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1175` n `12`; crypto_alt avg `0.2022` n `229`; crypto_major avg `0.3498` n `8`; equity avg `0.2293` n `91`; fx avg `-0.0369` n `6`; index avg `0.0342` n `25`; metal avg `-0.0255` n `20`; unknown avg `0.2327` n `763`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.0925` n `229`; crypto_major avg `0.3346` n `8`; equity avg `-0.3236` n `91`; fx avg `-0.0395` n `6`; index avg `-0.0809` n `25`; metal avg `-0.3681` n `20`; unknown avg `0.031` n `763`
- 4h: commodity avg `0.5561` n `12`; crypto_alt avg `-1.2784` n `229`; crypto_major avg `-0.8567` n `8`; equity avg `-1.8578` n `91`; fx avg `0.0136` n `6`; index avg `-0.3991` n `25`; metal avg `-1.1379` n `20`; unknown avg `-0.4866` n `743`
- 24h: commodity avg `1.3467` n `12`; crypto_alt avg `-3.6863` n `229`; crypto_major avg `-2.9721` n `8`; equity avg `-3.2925` n `91`; fx avg `-0.163` n `6`; index avg `-0.7364` n `25`; metal avg `-1.1771` n `20`; unknown avg `-0.841` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
