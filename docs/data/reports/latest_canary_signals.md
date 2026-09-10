# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T23:22:28.961888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.2103` n `233`; crypto_major avg `-0.0129` n `8`; equity avg `-0.0091` n `136`; fx avg `-0.0052` n `6`; index avg `-0.0015` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.0347` n `796`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `-1.0564` n `233`; crypto_major avg `-0.8231` n `8`; equity avg `-0.2225` n `136`; fx avg `-0.0034` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0037` n `20`; unknown avg `-0.1031` n `776`
- 4h: commodity avg `0.1758` n `12`; crypto_alt avg `-1.003` n `233`; crypto_major avg `-0.7632` n `8`; equity avg `-0.4321` n `136`; fx avg `0.0184` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0198` n `20`; unknown avg `-0.1617` n `716`
- 24h: commodity avg `1.0974` n `12`; crypto_alt avg `-2.4906` n `233`; crypto_major avg `-2.2796` n `8`; equity avg `-2.1286` n `136`; fx avg `0.1412` n `6`; index avg `-0.344` n `26`; metal avg `-1.2931` n `20`; unknown avg `-0.9589` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
