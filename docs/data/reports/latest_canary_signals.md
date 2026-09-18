# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T07:07:27.800260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.1188` n `234`; crypto_major avg `0.2628` n `8`; equity avg `0.0583` n `140`; fx avg `-0.0112` n `6`; index avg `-0.0004` n `26`; metal avg `0.026` n `20`; unknown avg `-0.1177` n `925`
- 1h: commodity avg `-0.0948` n `12`; crypto_alt avg `0.3716` n `234`; crypto_major avg `0.2538` n `8`; equity avg `0.2427` n `140`; fx avg `-0.0077` n `6`; index avg `0.0453` n `26`; metal avg `0.0501` n `20`; unknown avg `-0.123` n `907`
- 4h: commodity avg `-0.1782` n `12`; crypto_alt avg `1.1007` n `234`; crypto_major avg `1.2788` n `8`; equity avg `0.8497` n `140`; fx avg `-0.0022` n `6`; index avg `0.12` n `26`; metal avg `0.3097` n `20`; unknown avg `0.0015` n `863`
- 24h: commodity avg `-0.2239` n `12`; crypto_alt avg `4.9702` n `234`; crypto_major avg `3.7521` n `8`; equity avg `2.2925` n `140`; fx avg `0.1141` n `6`; index avg `0.308` n `26`; metal avg `0.6424` n `20`; unknown avg `2.291` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
