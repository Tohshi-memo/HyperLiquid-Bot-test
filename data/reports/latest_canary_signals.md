# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T00:09:49.203264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0772` n `12`; crypto_alt avg `0.2592` n `232`; crypto_major avg `0.1665` n `8`; equity avg `-0.0341` n `129`; fx avg `0.0237` n `6`; index avg `-0.0246` n `26`; metal avg `0.0924` n `20`; unknown avg `-0.1064` n `791`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `0.264` n `232`; crypto_major avg `0.2047` n `8`; equity avg `0.0101` n `129`; fx avg `0.019` n `6`; index avg `0.0093` n `26`; metal avg `0.1115` n `20`; unknown avg `-0.1585` n `791`
- 4h: commodity avg `0.1458` n `12`; crypto_alt avg `0.3405` n `232`; crypto_major avg `-0.2198` n `8`; equity avg `0.0362` n `129`; fx avg `0.0228` n `6`; index avg `-0.0029` n `26`; metal avg `0.0758` n `20`; unknown avg `0.7281` n `773`
- 24h: commodity avg `0.6301` n `12`; crypto_alt avg `2.4062` n `231`; crypto_major avg `2.0075` n `8`; equity avg `1.5408` n `129`; fx avg `-0.0864` n `6`; index avg `0.2403` n `26`; metal avg `-0.1495` n `20`; unknown avg `0.1985` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
