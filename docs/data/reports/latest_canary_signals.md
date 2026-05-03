# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T18:00:27.963356+00:00`
- Correlation status: `ready`
- Asset price records: `191`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1399` n `7`; crypto_alt avg `0.0299` n `223`; crypto_major avg `-0.0566` n `7`; equity avg `-0.007` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0146` n `9`; metal avg `-0.0467` n `7`; unknown avg `-0.0231` n `314`
- 1h: commodity avg `0.1713` n `7`; crypto_alt avg `0.2475` n `223`; crypto_major avg `0.1751` n `7`; equity avg `0.1071` n `42`; fx avg `-0.0056` n `4`; index avg `0.0131` n `9`; metal avg `0.0484` n `7`; unknown avg `-0.0163` n `313`
- 4h: commodity avg `-0.098` n `7`; crypto_alt avg `0.1695` n `223`; crypto_major avg `0.1269` n `7`; equity avg `0.2665` n `42`; fx avg `-0.0082` n `4`; index avg `0.0791` n `9`; metal avg `0.1977` n `7`; unknown avg `0.2349` n `313`
- 24h: commodity avg `-0.2334` n `7`; crypto_alt avg `0.0932` n `223`; crypto_major avg `0.1627` n `7`; equity avg `0.4589` n `42`; fx avg `0.0785` n `4`; index avg `0.0907` n `9`; metal avg `0.4063` n `7`; unknown avg `0.0432` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3996`, n `187`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3888`, n `183`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3827`, n `183`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3818`, n `187`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3767`, n `187`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3633`, n `187`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.328`, n `187`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3092`, n `187`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3045`, n `187`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.2742`, n `183`, moderate_sample_signal
