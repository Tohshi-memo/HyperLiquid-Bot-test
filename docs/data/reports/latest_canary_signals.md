# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T05:07:27.966309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.5143` n `234`; crypto_major avg `0.1538` n `8`; equity avg `0.0205` n `141`; fx avg `0.0019` n `6`; index avg `-0.0018` n `26`; metal avg `0.0025` n `20`; unknown avg `2.1384` n `959`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `0.1686` n `234`; crypto_major avg `-0.1505` n `8`; equity avg `0.0092` n `141`; fx avg `0.0093` n `6`; index avg `0.0069` n `26`; metal avg `-0.0096` n `20`; unknown avg `105.094` n `959`
- 4h: commodity avg `0.0631` n `12`; crypto_alt avg `0.0911` n `234`; crypto_major avg `-0.0937` n `8`; equity avg `0.0755` n `141`; fx avg `0.0013` n `6`; index avg `0.0173` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.0264` n `949`
- 24h: commodity avg `0.0123` n `12`; crypto_alt avg `0.6865` n `234`; crypto_major avg `-0.4187` n `8`; equity avg `0.1966` n `141`; fx avg `0.0161` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0142` n `20`; unknown avg `4.5849` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
