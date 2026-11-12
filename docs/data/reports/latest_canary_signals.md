# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T00:37:27.110137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.0756` n `239`; crypto_major avg `-0.0414` n `8`; equity avg `0.0596` n `161`; fx avg `0.0369` n `6`; index avg `0.0108` n `27`; metal avg `0.0428` n `20`; unknown avg `2.1484` n `1262`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `0.5182` n `239`; crypto_major avg `0.4138` n `8`; equity avg `-0.0206` n `161`; fx avg `-0.0338` n `6`; index avg `-0.0246` n `27`; metal avg `0.0396` n `20`; unknown avg `0.9506` n `1250`
- 4h: commodity avg `0.0436` n `13`; crypto_alt avg `-0.9966` n `239`; crypto_major avg `-0.8335` n `8`; equity avg `-1.4462` n `161`; fx avg `-0.0614` n `6`; index avg `-0.1381` n `27`; metal avg `-0.0911` n `20`; unknown avg `2.6876` n `1206`
- 24h: commodity avg `0.1973` n `13`; crypto_alt avg `-1.2621` n `239`; crypto_major avg `-0.0937` n `8`; equity avg `2.5768` n `161`; fx avg `-0.1421` n `6`; index avg `0.2627` n `27`; metal avg `-0.1624` n `20`; unknown avg `2.7863` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
