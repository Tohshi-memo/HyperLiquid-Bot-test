# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T07:07:25.542615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.095` n `229`; crypto_major avg `0.0784` n `8`; equity avg `0.0274` n `88`; fx avg `-0.0078` n `6`; index avg `0.0413` n `25`; metal avg `0.0537` n `20`; unknown avg `0.1252` n `765`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `0.07` n `229`; crypto_major avg `-0.1407` n `8`; equity avg `-0.0361` n `88`; fx avg `-0.075` n `6`; index avg `0.0281` n `25`; metal avg `0.0591` n `20`; unknown avg `-0.0956` n `763`
- 4h: commodity avg `0.1148` n `12`; crypto_alt avg `0.3651` n `229`; crypto_major avg `0.6329` n `8`; equity avg `0.5944` n `88`; fx avg `-0.1436` n `6`; index avg `0.2296` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.1928` n `743`
- 24h: commodity avg `0.5668` n `12`; crypto_alt avg `2.5687` n `228`; crypto_major avg `3.6832` n `8`; equity avg `0.6371` n `88`; fx avg `-0.1576` n `6`; index avg `0.2808` n `25`; metal avg `1.2809` n `20`; unknown avg `6.0282` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
