# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T16:22:29.781155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0048` n `229`; crypto_major avg `0.1583` n `8`; equity avg `0.0103` n `88`; fx avg `0.0046` n `6`; index avg `0.0199` n `25`; metal avg `0.0224` n `20`; unknown avg `-0.0786` n `765`
- 1h: commodity avg `0.0887` n `12`; crypto_alt avg `-0.0669` n `229`; crypto_major avg `0.0083` n `8`; equity avg `0.0349` n `88`; fx avg `-0.0138` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0825` n `20`; unknown avg `0.549` n `765`
- 4h: commodity avg `0.0893` n `12`; crypto_alt avg `0.2874` n `229`; crypto_major avg `0.6078` n `8`; equity avg `-0.0468` n `88`; fx avg `-0.0045` n `6`; index avg `-0.0123` n `25`; metal avg `-0.0293` n `20`; unknown avg `1.5125` n `765`
- 24h: commodity avg `0.2839` n `12`; crypto_alt avg `2.4498` n `229`; crypto_major avg `2.2845` n `8`; equity avg `1.8882` n `88`; fx avg `-0.0714` n `6`; index avg `0.4971` n `25`; metal avg `0.5645` n `20`; unknown avg `7.9134` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
