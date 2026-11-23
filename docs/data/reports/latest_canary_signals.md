# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T15:37:30.264209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.5397` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3929` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7794` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.5519` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.133` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `-0.2484` n `239`; crypto_major avg `-0.268` n `8`; equity avg `0.2983` n `166`; fx avg `-0.0055` n `6`; index avg `0.0024` n `27`; metal avg `-0.0261` n `20`; unknown avg `160.0905` n `1266`
- 1h: commodity avg `-0.5715` n `13`; crypto_alt avg `-0.9443` n `239`; crypto_major avg `-1.0224` n `8`; equity avg `0.5295` n `166`; fx avg `-0.0583` n `6`; index avg `0.1106` n `27`; metal avg `-0.0642` n `20`; unknown avg `1.7636` n `1266`
- 4h: commodity avg `-0.6047` n `13`; crypto_alt avg `2.9891` n `239`; crypto_major avg `3.935` n `8`; equity avg `5.7144` n `166`; fx avg `-0.1829` n `6`; index avg `0.603` n `27`; metal avg `0.5421` n `20`; unknown avg `10.143` n `1252`
- 24h: commodity avg `-1.5144` n `13`; crypto_alt avg `4.0362` n `239`; crypto_major avg `5.2385` n `8`; equity avg `7.8797` n `166`; fx avg `0.0026` n `6`; index avg `0.7059` n `27`; metal avg `0.9131` n `20`; unknown avg `10.82` n `1061`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
