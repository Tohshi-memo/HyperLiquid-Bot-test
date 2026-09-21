# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T08:07:32.148743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.0671` n `234`; crypto_major avg `0.3761` n `8`; equity avg `0.1763` n `140`; fx avg `-0.0196` n `6`; index avg `0.0301` n `26`; metal avg `0.0022` n `20`; unknown avg `6.42` n `936`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.0473` n `234`; crypto_major avg `0.3395` n `8`; equity avg `0.2281` n `140`; fx avg `-0.0193` n `6`; index avg `0.0341` n `26`; metal avg `-0.0489` n `20`; unknown avg `6.2335` n `936`
- 4h: commodity avg `0.0315` n `12`; crypto_alt avg `0.4811` n `234`; crypto_major avg `0.9222` n `8`; equity avg `0.4644` n `140`; fx avg `-0.0664` n `6`; index avg `0.1013` n `26`; metal avg `-0.0141` n `20`; unknown avg `1.927` n `890`
- 24h: commodity avg `-0.611` n `12`; crypto_alt avg `4.2106` n `234`; crypto_major avg `3.3091` n `8`; equity avg `1.5406` n `140`; fx avg `-0.0807` n `6`; index avg `0.3255` n `26`; metal avg `-0.0348` n `20`; unknown avg `3.6935` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
