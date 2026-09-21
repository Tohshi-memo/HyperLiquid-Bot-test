# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T07:52:32.388838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `12`; crypto_alt avg `0.2218` n `234`; crypto_major avg `0.0989` n `8`; equity avg `0.011` n `140`; fx avg `-0.0109` n `6`; index avg `0.0043` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.83` n `944`
- 1h: commodity avg `0.0119` n `12`; crypto_alt avg `-0.0472` n `234`; crypto_major avg `0.0662` n `8`; equity avg `0.1499` n `140`; fx avg `-0.0009` n `6`; index avg `0.0189` n `26`; metal avg `-0.0327` n `20`; unknown avg `0.6319` n `942`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `0.2171` n `234`; crypto_major avg `0.3019` n `8`; equity avg `0.1981` n `140`; fx avg `-0.0299` n `6`; index avg `0.0614` n `26`; metal avg `-0.0626` n `20`; unknown avg `0.4338` n `890`
- 24h: commodity avg `-0.6663` n `12`; crypto_alt avg `4.3646` n `234`; crypto_major avg `2.9983` n `8`; equity avg `1.3789` n `140`; fx avg `-0.0618` n `6`; index avg `0.2927` n `26`; metal avg `-0.0196` n `20`; unknown avg `3.2894` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
