# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T03:57:56.651908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0519` n `12`; crypto_alt avg `0.023` n `230`; crypto_major avg `0.114` n `8`; equity avg `0.0406` n `114`; fx avg `0.0023` n `6`; index avg `0.0083` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.0686` n `792`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `0.0508` n `8`; equity avg `0.103` n `114`; fx avg `-0.0021` n `6`; index avg `0.0234` n `25`; metal avg `-0.006` n `20`; unknown avg `-0.0213` n `792`
- 4h: commodity avg `-0.0292` n `12`; crypto_alt avg `0.7738` n `230`; crypto_major avg `1.1264` n `8`; equity avg `0.5866` n `114`; fx avg `-0.0131` n `6`; index avg `0.0283` n `25`; metal avg `0.2023` n `20`; unknown avg `0.8514` n `792`
- 24h: commodity avg `-0.1552` n `12`; crypto_alt avg `0.2679` n `230`; crypto_major avg `0.6836` n `8`; equity avg `0.7408` n `114`; fx avg `-0.0184` n `6`; index avg `0.0814` n `25`; metal avg `0.1943` n `20`; unknown avg `0.073` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
