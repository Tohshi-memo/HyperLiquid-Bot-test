# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T12:37:31.796285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `12`; crypto_alt avg `0.1673` n `234`; crypto_major avg `0.2696` n `8`; equity avg `0.005` n `140`; fx avg `-0.0101` n `6`; index avg `0.0028` n `26`; metal avg `0.0709` n `20`; unknown avg `0.8996` n `922`
- 1h: commodity avg `0.2011` n `12`; crypto_alt avg `0.1805` n `234`; crypto_major avg `0.1075` n `8`; equity avg `-0.309` n `140`; fx avg `-0.0108` n `6`; index avg `-0.0574` n `26`; metal avg `-0.1051` n `20`; unknown avg `1.732` n `920`
- 4h: commodity avg `0.1811` n `12`; crypto_alt avg `0.2804` n `234`; crypto_major avg `0.5386` n `8`; equity avg `-0.6972` n `140`; fx avg `-0.0247` n `6`; index avg `-0.1264` n `26`; metal avg `-0.092` n `20`; unknown avg `1.7271` n `917`
- 24h: commodity avg `0.2702` n `12`; crypto_alt avg `5.117` n `234`; crypto_major avg `3.7902` n `8`; equity avg `0.6547` n `140`; fx avg `0.2232` n `6`; index avg `-0.0439` n `26`; metal avg `0.2652` n `20`; unknown avg `2.6127` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
