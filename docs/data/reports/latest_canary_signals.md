# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T23:22:32.544462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.1707` n `233`; crypto_major avg `0.1531` n `8`; equity avg `0.0285` n `136`; fx avg `0.0082` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.1017` n `834`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `-0.0812` n `233`; crypto_major avg `-0.1827` n `8`; equity avg `0.0019` n `136`; fx avg `0.0071` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0168` n `20`; unknown avg `2.9509` n `828`
- 4h: commodity avg `-0.152` n `12`; crypto_alt avg `-0.2485` n `233`; crypto_major avg `-0.1776` n `8`; equity avg `-0.0117` n `136`; fx avg `-0.0235` n `6`; index avg `0.0011` n `26`; metal avg `-0.0244` n `20`; unknown avg `1.0097` n `788`
- 24h: commodity avg `-0.7528` n `12`; crypto_alt avg `0.7794` n `233`; crypto_major avg `1.3811` n `8`; equity avg `0.9253` n `136`; fx avg `-0.1872` n `6`; index avg `0.3297` n `26`; metal avg `0.2574` n `20`; unknown avg `2.0312` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
