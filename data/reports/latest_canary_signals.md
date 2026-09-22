# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T23:22:36.950165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `0.46` n `234`; crypto_major avg `0.0036` n `8`; equity avg `0.0416` n `140`; fx avg `-0.0019` n `6`; index avg `0.0054` n `26`; metal avg `0.0232` n `20`; unknown avg `0.9902` n `945`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `1.3498` n `234`; crypto_major avg `0.6041` n `8`; equity avg `0.0517` n `140`; fx avg `-0.0025` n `6`; index avg `0.0005` n `26`; metal avg `0.0445` n `20`; unknown avg `1.4833` n `943`
- 4h: commodity avg `-0.0271` n `12`; crypto_alt avg `1.7098` n `234`; crypto_major avg `0.1905` n `8`; equity avg `0.2104` n `140`; fx avg `-0.0324` n `6`; index avg `0.0164` n `26`; metal avg `0.0641` n `20`; unknown avg `1.7463` n `906`
- 24h: commodity avg `0.1308` n `12`; crypto_alt avg `3.4329` n `234`; crypto_major avg `0.5246` n `8`; equity avg `0.7421` n `140`; fx avg `-0.2846` n `6`; index avg `0.0962` n `26`; metal avg `0.2437` n `20`; unknown avg `1.3137` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
