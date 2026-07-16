# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T13:52:34.045565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `-0.1057` n `230`; crypto_major avg `-0.134` n `8`; equity avg `-0.6327` n `94`; fx avg `0.0042` n `6`; index avg `-0.0675` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.0353` n `768`
- 1h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.5051` n `230`; crypto_major avg `0.4802` n `8`; equity avg `-0.6797` n `94`; fx avg `0.0094` n `6`; index avg `0.0131` n `25`; metal avg `0.0662` n `20`; unknown avg `0.0816` n `768`
- 4h: commodity avg `0.2397` n `12`; crypto_alt avg `0.4757` n `230`; crypto_major avg `0.1094` n `8`; equity avg `-1.3838` n `94`; fx avg `0.0218` n `6`; index avg `-0.1738` n `25`; metal avg `-0.3442` n `20`; unknown avg `0.0902` n `768`
- 24h: commodity avg `0.1755` n `12`; crypto_alt avg `-0.9861` n `230`; crypto_major avg `-1.5211` n `8`; equity avg `-3.4315` n `93`; fx avg `0.0112` n `6`; index avg `-0.4518` n `25`; metal avg `-0.4992` n `20`; unknown avg `-0.1343` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
