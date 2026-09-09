# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T13:07:26.942764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.052` n `12`; crypto_alt avg `-0.0309` n `233`; crypto_major avg `-0.1523` n `8`; equity avg `0.0159` n `134`; fx avg `0.002` n `6`; index avg `0.0047` n `26`; metal avg `0.1654` n `20`; unknown avg `0.3026` n `797`
- 1h: commodity avg `-0.0543` n `12`; crypto_alt avg `0.3273` n `233`; crypto_major avg `0.2285` n `8`; equity avg `0.1539` n `134`; fx avg `-0.0116` n `6`; index avg `0.0319` n `26`; metal avg `0.2024` n `20`; unknown avg `0.6` n `790`
- 4h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.3128` n `233`; crypto_major avg `-0.1671` n `8`; equity avg `-0.6532` n `134`; fx avg `-0.0098` n `6`; index avg `-0.1478` n `26`; metal avg `0.1394` n `20`; unknown avg `13.6816` n `790`
- 24h: commodity avg `0.1139` n `12`; crypto_alt avg `0.5786` n `232`; crypto_major avg `1.5437` n `8`; equity avg `0.1048` n `134`; fx avg `-0.0843` n `6`; index avg `-0.2249` n `26`; metal avg `0.0316` n `20`; unknown avg `1.275` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
