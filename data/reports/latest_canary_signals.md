# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T19:07:32.213054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.2742` n `234`; crypto_major avg `0.1926` n `8`; equity avg `0.0252` n `140`; fx avg `-0.0122` n `6`; index avg `-0.0032` n `26`; metal avg `0.0002` n `20`; unknown avg `0.3894` n `941`
- 1h: commodity avg `0.0038` n `12`; crypto_alt avg `-0.2133` n `234`; crypto_major avg `0.0823` n `8`; equity avg `-0.0146` n `140`; fx avg `-0.0102` n `6`; index avg `0.0003` n `26`; metal avg `-0.0169` n `20`; unknown avg `1.1346` n `933`
- 4h: commodity avg `0.0179` n `12`; crypto_alt avg `1.9929` n `234`; crypto_major avg `1.1201` n `8`; equity avg `0.2171` n `140`; fx avg `-0.03` n `6`; index avg `0.0283` n `26`; metal avg `-0.0124` n `20`; unknown avg `1.5181` n `871`
- 24h: commodity avg `0.3541` n `12`; crypto_alt avg `0.0345` n `234`; crypto_major avg `-0.7605` n `8`; equity avg `-0.0912` n `140`; fx avg `-0.0462` n `6`; index avg `-0.0412` n `26`; metal avg `-0.0508` n `20`; unknown avg `62.5974` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
