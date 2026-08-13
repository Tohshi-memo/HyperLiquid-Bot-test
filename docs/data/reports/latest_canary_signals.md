# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T19:41:16.288186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0108` n `230`; crypto_major avg `-0.0069` n `8`; equity avg `-0.1657` n `113`; fx avg `0.001` n `6`; index avg `-0.0242` n `25`; metal avg `0.0235` n `20`; unknown avg `0.0002` n `787`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `0.2168` n `230`; crypto_major avg `0.3561` n `8`; equity avg `-0.0739` n `113`; fx avg `0.0041` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0986` n `20`; unknown avg `0.2556` n `787`
- 4h: commodity avg `-0.2419` n `12`; crypto_alt avg `-0.5951` n `230`; crypto_major avg `-0.064` n `8`; equity avg `-0.0061` n `113`; fx avg `-0.0008` n `6`; index avg `0.0382` n `25`; metal avg `-0.0921` n `20`; unknown avg `-0.0992` n `787`
- 24h: commodity avg `-0.4997` n `12`; crypto_alt avg `-0.2516` n `230`; crypto_major avg `0.3268` n `8`; equity avg `1.3511` n `113`; fx avg `0.0133` n `6`; index avg `0.313` n `25`; metal avg `-0.5259` n `20`; unknown avg `0.0583` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.234`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
