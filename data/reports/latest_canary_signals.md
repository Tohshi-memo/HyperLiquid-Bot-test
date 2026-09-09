# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T09:37:30.819881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.2244` n `233`; crypto_major avg `-0.2052` n `8`; equity avg `-0.2897` n `134`; fx avg `-0.0073` n `6`; index avg `-0.0414` n `26`; metal avg `0.0053` n `20`; unknown avg `0.8526` n `798`
- 1h: commodity avg `0.045` n `12`; crypto_alt avg `-0.4722` n `233`; crypto_major avg `-0.3914` n `8`; equity avg `-0.4071` n `134`; fx avg `-0.0301` n `6`; index avg `-0.0683` n `26`; metal avg `-0.035` n `20`; unknown avg `14.54` n `796`
- 4h: commodity avg `0.2311` n `12`; crypto_alt avg `0.394` n `233`; crypto_major avg `0.2177` n `8`; equity avg `-0.0625` n `134`; fx avg `0.0115` n `6`; index avg `-0.0546` n `26`; metal avg `0.0651` n `20`; unknown avg `2.1945` n `772`
- 24h: commodity avg `-0.1177` n `12`; crypto_alt avg `-0.1366` n `232`; crypto_major avg `0.8603` n `8`; equity avg `0.8703` n `134`; fx avg `-0.1184` n `6`; index avg `-0.0429` n `26`; metal avg `-0.0009` n `20`; unknown avg `1.9353` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
