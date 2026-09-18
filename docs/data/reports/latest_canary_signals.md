# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T02:37:31.895639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.2959` n `234`; crypto_major avg `0.3233` n `8`; equity avg `0.0772` n `140`; fx avg `-0.0193` n `6`; index avg `0.0035` n `26`; metal avg `0.0304` n `20`; unknown avg `-0.4124` n `919`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.7914` n `234`; crypto_major avg `0.5231` n `8`; equity avg `0.1985` n `140`; fx avg `-0.0138` n `6`; index avg `0.0239` n `26`; metal avg `0.0302` n `20`; unknown avg `-0.5037` n `917`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `2.1419` n `234`; crypto_major avg `1.4197` n `8`; equity avg `0.0392` n `140`; fx avg `0.0659` n `6`; index avg `-0.0675` n `26`; metal avg `0.1625` n `20`; unknown avg `-0.4438` n `891`
- 24h: commodity avg `-0.2318` n `12`; crypto_alt avg `4.5826` n `234`; crypto_major avg `2.7133` n `8`; equity avg `1.6012` n `139`; fx avg `0.0366` n `6`; index avg `0.211` n `26`; metal avg `0.532` n `20`; unknown avg `1.8193` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
