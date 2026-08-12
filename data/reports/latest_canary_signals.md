# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T02:52:28.328402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `0.1067` n `230`; crypto_major avg `0.019` n `8`; equity avg `0.0642` n `113`; fx avg `-0.0032` n `6`; index avg `0.0115` n `25`; metal avg `0.0268` n `20`; unknown avg `-0.0861` n `786`
- 1h: commodity avg `0.0608` n `12`; crypto_alt avg `0.0851` n `230`; crypto_major avg `-0.2055` n `8`; equity avg `0.3131` n `113`; fx avg `0.0085` n `6`; index avg `0.0588` n `25`; metal avg `0.1018` n `20`; unknown avg `-0.2479` n `786`
- 4h: commodity avg `0.1295` n `12`; crypto_alt avg `0.394` n `230`; crypto_major avg `0.1682` n `8`; equity avg `0.7943` n `113`; fx avg `0.0402` n `6`; index avg `0.158` n `25`; metal avg `0.2193` n `20`; unknown avg `-0.1274` n `786`
- 24h: commodity avg `0.2375` n `12`; crypto_alt avg `-0.9083` n `230`; crypto_major avg `0.685` n `8`; equity avg `1.6707` n `113`; fx avg `0.0139` n `6`; index avg `0.1536` n `25`; metal avg `-0.0558` n `20`; unknown avg `-0.0694` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2257`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2188`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
