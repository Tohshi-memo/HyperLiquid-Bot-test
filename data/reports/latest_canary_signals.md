# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T19:22:25.317000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.0169` n `230`; crypto_major avg `0.0253` n `8`; equity avg `0.0941` n `103`; fx avg `0.0055` n `6`; index avg `-0.0039` n `25`; metal avg `0.0257` n `20`; unknown avg `0.5923` n `784`
- 1h: commodity avg `0.0964` n `12`; crypto_alt avg `-0.0603` n `230`; crypto_major avg `-0.1287` n `8`; equity avg `-0.0256` n `103`; fx avg `0.0062` n `6`; index avg `-0.0024` n `25`; metal avg `0.0865` n `20`; unknown avg `0.3422` n `784`
- 4h: commodity avg `0.1239` n `12`; crypto_alt avg `0.4345` n `230`; crypto_major avg `0.2119` n `8`; equity avg `1.0388` n `103`; fx avg `-0.0128` n `6`; index avg `0.1741` n `25`; metal avg `0.1312` n `20`; unknown avg `-0.0499` n `784`
- 24h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.462` n `230`; crypto_major avg `0.5739` n `8`; equity avg `1.976` n `103`; fx avg `-0.2306` n `6`; index avg `0.0755` n `25`; metal avg `-0.3853` n `20`; unknown avg `0.0271` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
