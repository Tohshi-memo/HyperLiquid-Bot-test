# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T22:37:28.865095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.0637` n `230`; crypto_major avg `-0.0768` n `8`; equity avg `-0.0057` n `113`; fx avg `0.0023` n `6`; index avg `-0.0068` n `25`; metal avg `-0.02` n `20`; unknown avg `-0.1159` n `786`
- 1h: commodity avg `-0.0634` n `12`; crypto_alt avg `-0.1756` n `230`; crypto_major avg `-0.0948` n `8`; equity avg `-0.1263` n `113`; fx avg `0.0027` n `6`; index avg `-0.0168` n `25`; metal avg `-0.0699` n `20`; unknown avg `-0.1458` n `786`
- 4h: commodity avg `-0.134` n `12`; crypto_alt avg `-1.0686` n `230`; crypto_major avg `-0.6257` n `8`; equity avg `-0.4614` n `113`; fx avg `-0.013` n `6`; index avg `-0.0278` n `25`; metal avg `-0.1336` n `20`; unknown avg `-0.3454` n `786`
- 24h: commodity avg `-0.0488` n `12`; crypto_alt avg `-1.6585` n `230`; crypto_major avg `-0.6746` n `8`; equity avg `2.7668` n `113`; fx avg `0.0131` n `6`; index avg `0.3929` n `25`; metal avg `0.0542` n `20`; unknown avg `-0.0974` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2336`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
