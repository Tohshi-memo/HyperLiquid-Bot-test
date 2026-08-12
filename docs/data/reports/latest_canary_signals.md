# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T03:52:34.864113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `-0.136` n `230`; crypto_major avg `-0.0494` n `8`; equity avg `-0.0286` n `113`; fx avg `-0.0115` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.0535` n `786`
- 1h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.15` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `0.0926` n `113`; fx avg `0.0041` n `6`; index avg `0.0059` n `25`; metal avg `-0.0308` n `20`; unknown avg `0.6279` n `786`
- 4h: commodity avg `0.2115` n `12`; crypto_alt avg `0.2925` n `230`; crypto_major avg `0.0549` n `8`; equity avg `0.8151` n `113`; fx avg `0.0457` n `6`; index avg `0.1541` n `25`; metal avg `0.2032` n `20`; unknown avg `-0.2037` n `786`
- 24h: commodity avg `0.3474` n `12`; crypto_alt avg `-1.075` n `230`; crypto_major avg `0.606` n `8`; equity avg `1.6776` n `113`; fx avg `0.0198` n `6`; index avg `0.1337` n `25`; metal avg `-0.1316` n `20`; unknown avg `-0.1092` n `753`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2245`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2158`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.21`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
