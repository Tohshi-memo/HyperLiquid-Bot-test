# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T12:07:24.178206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0392` n `12`; crypto_alt avg `-0.0643` n `234`; crypto_major avg `0.0279` n `8`; equity avg `-0.0185` n `140`; fx avg `0.0055` n `6`; index avg `-0.0056` n `26`; metal avg `0.0587` n `20`; unknown avg `0.029` n `936`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.3231` n `234`; crypto_major avg `0.2853` n `8`; equity avg `-0.2407` n `140`; fx avg `0.004` n `6`; index avg `-0.0238` n `26`; metal avg `0.0386` n `20`; unknown avg `6.0385` n `936`
- 4h: commodity avg `-0.474` n `12`; crypto_alt avg `-0.4103` n `234`; crypto_major avg `0.3398` n `8`; equity avg `0.4521` n `140`; fx avg `-0.1149` n `6`; index avg `0.092` n `26`; metal avg `0.1924` n `20`; unknown avg `3.9146` n `934`
- 24h: commodity avg `-0.4616` n `12`; crypto_alt avg `0.1006` n `234`; crypto_major avg `1.1653` n `8`; equity avg `0.6909` n `140`; fx avg `-0.2907` n `6`; index avg `0.2091` n `26`; metal avg `-0.225` n `20`; unknown avg `1112.333` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
