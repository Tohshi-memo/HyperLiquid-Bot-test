# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T03:37:22.900569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `0.0373` n `8`; equity avg `0.0341` n `113`; fx avg `-0.0084` n `6`; index avg `-0.0085` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0748` n `786`
- 1h: commodity avg `0.0389` n `12`; crypto_alt avg `0.0923` n `230`; crypto_major avg `0.0248` n `8`; equity avg `0.1862` n `113`; fx avg `0.0124` n `6`; index avg `0.0303` n `25`; metal avg `0.0078` n `20`; unknown avg `0.1384` n `786`
- 4h: commodity avg `0.1612` n `12`; crypto_alt avg `0.4306` n `230`; crypto_major avg `0.1015` n `8`; equity avg `0.8907` n `113`; fx avg `0.0561` n `6`; index avg `0.1793` n `25`; metal avg `0.2187` n `20`; unknown avg `-0.1876` n `786`
- 24h: commodity avg `0.284` n `12`; crypto_alt avg `-0.936` n `230`; crypto_major avg `0.6027` n `8`; equity avg `1.8238` n `113`; fx avg `0.0313` n `6`; index avg `0.1542` n `25`; metal avg `-0.1347` n `20`; unknown avg `0.0323` n `753`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
