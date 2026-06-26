# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T23:37:25.813238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `0.0971` n `8`; equity avg `0.0432` n `88`; fx avg `-0.0578` n `6`; index avg `0.0137` n `23`; metal avg `0.0072` n `20`; unknown avg `0.0169` n `764`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.2157` n `228`; crypto_major avg `0.2575` n `8`; equity avg `0.1401` n `88`; fx avg `-0.0205` n `6`; index avg `0.0214` n `23`; metal avg `0.0508` n `20`; unknown avg `0.0644` n `764`
- 4h: commodity avg `0.1896` n `12`; crypto_alt avg `-0.4345` n `228`; crypto_major avg `-0.3262` n `8`; equity avg `0.2853` n `88`; fx avg `0.0503` n `6`; index avg `-0.0264` n `23`; metal avg `0.1329` n `20`; unknown avg `-0.2527` n `748`
- 24h: commodity avg `-0.2503` n `12`; crypto_alt avg `1.1982` n `228`; crypto_major avg `0.7941` n `8`; equity avg `-0.4959` n `87`; fx avg `0.0041` n `6`; index avg `-0.4003` n `23`; metal avg `0.7211` n `20`; unknown avg `0.0589` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
