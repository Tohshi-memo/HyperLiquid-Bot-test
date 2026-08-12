# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T01:22:26.743489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0244` n `230`; crypto_major avg `-0.1344` n `8`; equity avg `0.0071` n `113`; fx avg `0.0116` n `6`; index avg `0.0083` n `25`; metal avg `0.0153` n `20`; unknown avg `-0.0545` n `786`
- 1h: commodity avg `0.0634` n `12`; crypto_alt avg `0.1074` n `230`; crypto_major avg `0.1321` n `8`; equity avg `-0.0214` n `113`; fx avg `-0.013` n `6`; index avg `0.0057` n `25`; metal avg `0.0821` n `20`; unknown avg `-0.0419` n `786`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `0.2673` n `230`; crypto_major avg `0.234` n `8`; equity avg `0.2532` n `113`; fx avg `0.0106` n `6`; index avg `0.0301` n `25`; metal avg `0.1293` n `20`; unknown avg `-0.0854` n `786`
- 24h: commodity avg `0.2549` n `12`; crypto_alt avg `-1.2139` n `230`; crypto_major avg `0.7966` n `8`; equity avg `1.1003` n `113`; fx avg `-0.0024` n `6`; index avg `0.0556` n `25`; metal avg `-0.2963` n `20`; unknown avg `-0.0819` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2211`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
