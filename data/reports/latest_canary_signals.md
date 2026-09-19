# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T12:22:29.649723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.1492` n `234`; crypto_major avg `-0.1194` n `8`; equity avg `0.0` n `140`; fx avg `-0.0071` n `6`; index avg `0.0014` n `26`; metal avg `0.0019` n `20`; unknown avg `0.2442` n `942`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `0.097` n `234`; crypto_major avg `0.0159` n `8`; equity avg `0.0106` n `140`; fx avg `-0.0245` n `6`; index avg `0.0126` n `26`; metal avg `0.0055` n `20`; unknown avg `0.3422` n `934`
- 4h: commodity avg `-0.0123` n `12`; crypto_alt avg `1.0339` n `234`; crypto_major avg `0.1251` n `8`; equity avg `-0.004` n `140`; fx avg `-0.0099` n `6`; index avg `0.0163` n `26`; metal avg `0.0153` n `20`; unknown avg `0.9242` n `934`
- 24h: commodity avg `0.0242` n `12`; crypto_alt avg `4.3077` n `234`; crypto_major avg `4.0106` n `8`; equity avg `0.7689` n `140`; fx avg `-0.0227` n `6`; index avg `0.0657` n `26`; metal avg `-0.0314` n `20`; unknown avg `2.7245` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
