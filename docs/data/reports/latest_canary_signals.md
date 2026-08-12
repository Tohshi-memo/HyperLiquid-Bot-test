# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T02:22:36.081435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0464` n `230`; crypto_major avg `-0.2155` n `8`; equity avg `0.1025` n `113`; fx avg `0.0066` n `6`; index avg `0.0242` n `25`; metal avg `0.0556` n `20`; unknown avg `-0.0938` n `786`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.1088` n `230`; crypto_major avg `0.0251` n `8`; equity avg `0.3314` n `113`; fx avg `0.0343` n `6`; index avg `0.0596` n `25`; metal avg `0.041` n `20`; unknown avg `-0.09` n `786`
- 4h: commodity avg `0.0599` n `12`; crypto_alt avg `0.1755` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `0.6144` n `113`; fx avg `0.0366` n `6`; index avg `0.0969` n `25`; metal avg `0.1234` n `20`; unknown avg `-0.2346` n `786`
- 24h: commodity avg `0.2067` n `12`; crypto_alt avg `-1.2027` n `230`; crypto_major avg `0.6805` n `8`; equity avg `1.5817` n `113`; fx avg `-0.0016` n `6`; index avg `0.1198` n `25`; metal avg `-0.2689` n `20`; unknown avg `-0.0565` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2247`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
