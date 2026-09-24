# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T07:37:31.923854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.3805` n `234`; crypto_major avg `0.5954` n `8`; equity avg `0.2035` n `141`; fx avg `-0.0252` n `6`; index avg `0.0231` n `26`; metal avg `0.0499` n `20`; unknown avg `1.3554` n `945`
- 1h: commodity avg `-0.1322` n `12`; crypto_alt avg `0.2265` n `234`; crypto_major avg `0.5497` n `8`; equity avg `0.2192` n `141`; fx avg `-0.0149` n `6`; index avg `0.0419` n `26`; metal avg `0.1302` n `20`; unknown avg `1.8904` n `943`
- 4h: commodity avg `0.144` n `12`; crypto_alt avg `1.1851` n `234`; crypto_major avg `1.0961` n `8`; equity avg `-0.1271` n `141`; fx avg `-0.0062` n `6`; index avg `-0.0312` n `26`; metal avg `0.1416` n `20`; unknown avg `1.1572` n `921`
- 24h: commodity avg `0.523` n `12`; crypto_alt avg `-3.4759` n `234`; crypto_major avg `-2.927` n `8`; equity avg `-1.8812` n `140`; fx avg `-0.0427` n `6`; index avg `-0.3876` n `26`; metal avg `-0.289` n `20`; unknown avg `587.2012` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
