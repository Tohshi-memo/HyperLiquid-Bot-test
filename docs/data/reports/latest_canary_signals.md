# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T22:42:22.679595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `0.0531` n `229`; crypto_major avg `0.0679` n `8`; equity avg `0.0343` n `91`; fx avg `-0.0193` n `6`; index avg `0.0288` n `25`; metal avg `0.0287` n `20`; unknown avg `0.0518` n `764`
- 1h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.3157` n `229`; crypto_major avg `0.2564` n `8`; equity avg `0.1365` n `91`; fx avg `-0.0004` n `6`; index avg `0.0416` n `25`; metal avg `0.0809` n `20`; unknown avg `0.0634` n `764`
- 4h: commodity avg `0.1626` n `12`; crypto_alt avg `0.2735` n `229`; crypto_major avg `0.3956` n `8`; equity avg `0.637` n `91`; fx avg `0.0101` n `6`; index avg `0.0748` n `25`; metal avg `0.0115` n `20`; unknown avg `1.1574` n `764`
- 24h: commodity avg `0.3515` n `12`; crypto_alt avg `-1.6453` n `229`; crypto_major avg `-2.4043` n `8`; equity avg `1.4424` n `91`; fx avg `0.0425` n `6`; index avg `0.0252` n `25`; metal avg `-0.6692` n `20`; unknown avg `0.0053` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
