# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T09:37:24.984322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2821` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.0255` n `234`; crypto_major avg `-0.0636` n `8`; equity avg `-0.061` n `141`; fx avg `0.0011` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0495` n `20`; unknown avg `0.3905` n `945`
- 1h: commodity avg `-0.1253` n `12`; crypto_alt avg `-0.9903` n `234`; crypto_major avg `-0.893` n `8`; equity avg `-0.1435` n `141`; fx avg `-0.0032` n `6`; index avg `-0.0199` n `26`; metal avg `-0.0689` n `20`; unknown avg `-0.1105` n `943`
- 4h: commodity avg `0.312` n `12`; crypto_alt avg `-1.7604` n `234`; crypto_major avg `-1.4515` n `8`; equity avg `-1.1763` n `141`; fx avg `0.0527` n `6`; index avg `-0.1694` n `26`; metal avg `-0.211` n `20`; unknown avg `2.4348` n `921`
- 24h: commodity avg `0.7082` n `12`; crypto_alt avg `-5.2397` n `234`; crypto_major avg `-4.1163` n `8`; equity avg `-2.8477` n `140`; fx avg `0.044` n `6`; index avg `-0.5117` n `26`; metal avg `-0.5321` n `20`; unknown avg `587.7397` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
