# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T09:22:26.639714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `-0.0276` n `229`; crypto_major avg `-0.0791` n `8`; equity avg `0.0579` n `88`; fx avg `-0.0036` n `6`; index avg `0.0136` n `25`; metal avg `-0.0186` n `20`; unknown avg `0.1388` n `765`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `0.145` n `229`; crypto_major avg `0.1693` n `8`; equity avg `0.0049` n `88`; fx avg `0.0144` n `6`; index avg `-0.0164` n `25`; metal avg `-0.0734` n `20`; unknown avg `0.1452` n `765`
- 4h: commodity avg `-0.0534` n `12`; crypto_alt avg `0.7881` n `229`; crypto_major avg `0.5976` n `8`; equity avg `0.2476` n `88`; fx avg `-0.1665` n `6`; index avg `0.054` n `25`; metal avg `0.0887` n `20`; unknown avg `0.0831` n `743`
- 24h: commodity avg `0.4788` n `12`; crypto_alt avg `2.2796` n `228`; crypto_major avg `3.3761` n `8`; equity avg `0.2848` n `88`; fx avg `-0.1186` n `6`; index avg `0.2067` n `25`; metal avg `1.2057` n `20`; unknown avg `5.3151` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
