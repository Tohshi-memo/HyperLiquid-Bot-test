# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T12:52:25.113299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `-0.1417` n `233`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0` n `136`; fx avg `0.0033` n `6`; index avg `0.0008` n `26`; metal avg `0.0045` n `20`; unknown avg `1.8639` n `832`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.052` n `233`; crypto_major avg `-0.1006` n `8`; equity avg `0.0036` n `136`; fx avg `0.0027` n `6`; index avg `0.0024` n `26`; metal avg `-0.0015` n `20`; unknown avg `2.7253` n `824`
- 4h: commodity avg `0.0556` n `12`; crypto_alt avg `0.1337` n `233`; crypto_major avg `0.234` n `8`; equity avg `0.069` n `136`; fx avg `-0.009` n `6`; index avg `-0.0021` n `26`; metal avg `0.0323` n `20`; unknown avg `0.9421` n `824`
- 24h: commodity avg `-0.0865` n `12`; crypto_alt avg `0.8054` n `233`; crypto_major avg `-0.0291` n `8`; equity avg `-0.4661` n `136`; fx avg `0.0011` n `6`; index avg `0.0005` n `26`; metal avg `-0.195` n `20`; unknown avg `9.8817` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
