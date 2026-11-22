# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T12:07:37.226071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1698` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0297` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.0597` n `239`; crypto_major avg `0.0096` n `8`; equity avg `0.0058` n `166`; fx avg `0.0013` n `6`; index avg `-0.0025` n `27`; metal avg `0.0225` n `20`; unknown avg `-0.0119` n `1251`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `-0.0145` n `239`; crypto_major avg `-0.0679` n `8`; equity avg `0.0514` n `166`; fx avg `0.0078` n `6`; index avg `-0.0175` n `27`; metal avg `0.0103` n `20`; unknown avg `159.3465` n `1253`
- 4h: commodity avg `0.0248` n `13`; crypto_alt avg `1.7575` n `239`; crypto_major avg `2.1946` n `8`; equity avg `1.1959` n `166`; fx avg `-0.0082` n `6`; index avg `0.0982` n `27`; metal avg `0.1649` n `20`; unknown avg `136.547` n `1141`
- 24h: commodity avg `0.0498` n `13`; crypto_alt avg `3.0295` n `239`; crypto_major avg `3.4174` n `8`; equity avg `1.8683` n `166`; fx avg `-0.0033` n `6`; index avg `0.2133` n `27`; metal avg `0.1894` n `20`; unknown avg `0.6228` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
