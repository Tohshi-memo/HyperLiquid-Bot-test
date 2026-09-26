# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T05:37:29.319311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.015` n `234`; crypto_major avg `-0.0883` n `8`; equity avg `-0.0223` n `141`; fx avg `0.0007` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.21` n `961`
- 1h: commodity avg `-0.0317` n `12`; crypto_alt avg `0.1858` n `234`; crypto_major avg `-0.0826` n `8`; equity avg `0.0279` n `141`; fx avg `-0.0088` n `6`; index avg `0.0046` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.3239` n `959`
- 4h: commodity avg `-0.1117` n `12`; crypto_alt avg `-0.295` n `234`; crypto_major avg `-0.7097` n `8`; equity avg `0.0483` n `141`; fx avg `-0.0046` n `6`; index avg `0.0124` n `26`; metal avg `0.009` n `20`; unknown avg `15.0309` n `952`
- 24h: commodity avg `0.0525` n `12`; crypto_alt avg `3.1528` n `234`; crypto_major avg `0.8564` n `8`; equity avg `-0.5261` n `141`; fx avg `-0.0893` n `6`; index avg `0.0789` n `26`; metal avg `0.2114` n `20`; unknown avg `1126.8373` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
