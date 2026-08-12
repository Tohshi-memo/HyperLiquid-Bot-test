# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T02:42:22.720419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `0.0371` n `230`; crypto_major avg `-0.0062` n `8`; equity avg `0.1761` n `113`; fx avg `0.0032` n `6`; index avg `0.0502` n `25`; metal avg `0.0447` n `20`; unknown avg `-0.0848` n `786`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `0.1256` n `230`; crypto_major avg `0.0407` n `8`; equity avg `0.4281` n `113`; fx avg `0.0226` n `6`; index avg `0.0798` n `25`; metal avg `0.1234` n `20`; unknown avg `-0.1425` n `786`
- 4h: commodity avg `0.1121` n `12`; crypto_alt avg `0.2402` n `230`; crypto_major avg `0.0553` n `8`; equity avg `0.7747` n `113`; fx avg `0.0379` n `6`; index avg `0.1526` n `25`; metal avg `0.1684` n `20`; unknown avg `-0.2513` n `786`
- 24h: commodity avg `0.2496` n `12`; crypto_alt avg `-1.0589` n `230`; crypto_major avg `0.7014` n `8`; equity avg `1.6558` n `113`; fx avg `0.0082` n `6`; index avg `0.1523` n `25`; metal avg `-0.1426` n `20`; unknown avg `-0.0568` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2253`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2215`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
