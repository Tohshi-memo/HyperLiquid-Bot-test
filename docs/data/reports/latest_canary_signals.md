# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T04:22:27.456211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.0116` n `233`; crypto_major avg `0.0035` n `8`; equity avg `0.0057` n `136`; fx avg `0.0006` n `6`; index avg `0.0008` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.6615` n `838`
- 1h: commodity avg `0.038` n `12`; crypto_alt avg `-0.0027` n `233`; crypto_major avg `-0.1855` n `8`; equity avg `-0.0549` n `136`; fx avg `0.0063` n `6`; index avg `-0.0009` n `26`; metal avg `0.003` n `20`; unknown avg `0.993` n `836`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.2612` n `233`; crypto_major avg `-0.1249` n `8`; equity avg `-0.1661` n `136`; fx avg `0.0069` n `6`; index avg `-0.0269` n `26`; metal avg `0.0033` n `20`; unknown avg `3.1225` n `806`
- 24h: commodity avg `0.1026` n `12`; crypto_alt avg `1.0363` n `233`; crypto_major avg `0.0554` n `8`; equity avg `-0.4805` n `136`; fx avg `-0.0071` n `6`; index avg `-0.0603` n `26`; metal avg `0.0478` n `20`; unknown avg `-0.3241` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
