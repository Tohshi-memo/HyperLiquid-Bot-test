# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T04:37:30.680436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `0.101` n `233`; crypto_major avg `0.144` n `8`; equity avg `0.1868` n `136`; fx avg `0.0023` n `6`; index avg `0.0535` n `26`; metal avg `0.0307` n `20`; unknown avg `4.807` n `790`
- 1h: commodity avg `-0.0708` n `12`; crypto_alt avg `0.7901` n `233`; crypto_major avg `0.4541` n `8`; equity avg `0.3278` n `136`; fx avg `-0.0309` n `6`; index avg `0.1023` n `26`; metal avg `0.1294` n `20`; unknown avg `27.2256` n `788`
- 4h: commodity avg `-0.0938` n `12`; crypto_alt avg `0.6385` n `233`; crypto_major avg `0.5608` n `8`; equity avg `-0.1211` n `136`; fx avg `-0.0761` n `6`; index avg `0.0486` n `26`; metal avg `0.0621` n `20`; unknown avg `-0.4599` n `780`
- 24h: commodity avg `1.1045` n `12`; crypto_alt avg `-1.4946` n `233`; crypto_major avg `-2.0809` n `8`; equity avg `-1.9298` n `136`; fx avg `0.0682` n `6`; index avg `-0.2916` n `26`; metal avg `-1.2201` n `20`; unknown avg `-0.4069` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
