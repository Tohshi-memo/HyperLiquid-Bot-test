# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T07:37:33.762165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `-0.0979` n `234`; crypto_major avg `-0.1545` n `8`; equity avg `0.0483` n `140`; fx avg `-0.0115` n `6`; index avg `0.0063` n `26`; metal avg `-0.0096` n `20`; unknown avg `2.4827` n `944`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.261` n `234`; crypto_major avg `-0.072` n `8`; equity avg `0.1715` n `140`; fx avg `0.0068` n `6`; index avg `0.0185` n `26`; metal avg `0.0109` n `20`; unknown avg `2.06` n `928`
- 4h: commodity avg `0.0373` n `12`; crypto_alt avg `0.3398` n `234`; crypto_major avg `0.184` n `8`; equity avg `0.2494` n `140`; fx avg `-0.0142` n `6`; index avg `0.0671` n `26`; metal avg `-0.0666` n `20`; unknown avg `1.6043` n `890`
- 24h: commodity avg `-0.6511` n `12`; crypto_alt avg `4.0429` n `234`; crypto_major avg `2.8277` n `8`; equity avg `1.3514` n `140`; fx avg `-0.0609` n `6`; index avg `0.2873` n `26`; metal avg `-0.0157` n `20`; unknown avg `2.6415` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
