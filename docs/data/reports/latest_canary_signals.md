# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T15:37:34.024757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.133` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `-0.3915` n `234`; crypto_major avg `-0.1795` n `8`; equity avg `-0.001` n `141`; fx avg `-0.0094` n `6`; index avg `0.021` n `26`; metal avg `0.0224` n `20`; unknown avg `0.5654` n `963`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `-1.3681` n `234`; crypto_major avg `-1.2168` n `8`; equity avg `-0.5819` n `141`; fx avg `-0.002` n `6`; index avg `-0.0838` n `26`; metal avg `-0.0706` n `20`; unknown avg `2.9675` n `927`
- 4h: commodity avg `-0.1604` n `12`; crypto_alt avg `-0.8645` n `234`; crypto_major avg `-1.0629` n `8`; equity avg `0.0912` n `141`; fx avg `-0.0182` n `6`; index avg `-0.0725` n `26`; metal avg `-0.175` n `20`; unknown avg `225.1414` n `893`
- 24h: commodity avg `-0.8093` n `12`; crypto_alt avg `1.5661` n `234`; crypto_major avg `-0.0414` n `8`; equity avg `1.0991` n `141`; fx avg `-0.1462` n `6`; index avg `0.0697` n `26`; metal avg `-0.0672` n `20`; unknown avg `14.5129` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
