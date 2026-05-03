# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:00:29.593974+00:00`
- Correlation status: `ready`
- Asset price records: `163`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `7`; crypto_alt avg `-0.3592` n `223`; crypto_major avg `-0.2204` n `7`; equity avg `0.0424` n `42`; fx avg `0.0003` n `4`; index avg `-0.0445` n `9`; metal avg `0.0078` n `7`; unknown avg `-0.1007` n `313`
- 1h: commodity avg `-0.0588` n `7`; crypto_alt avg `-0.3843` n `223`; crypto_major avg `-0.2846` n `7`; equity avg `0.1061` n `42`; fx avg `0.005` n `4`; index avg `-0.0163` n `9`; metal avg `0.0194` n `7`; unknown avg `-0.1338` n `313`
- 4h: commodity avg `-0.0661` n `7`; crypto_alt avg `0.017` n `223`; crypto_major avg `0.0483` n `7`; equity avg `0.0716` n `42`; fx avg `0.0204` n `4`; index avg `-0.0111` n `9`; metal avg `0.1213` n `7`; unknown avg `-0.2183` n `313`
- 24h: commodity avg `-0.3195` n `7`; crypto_alt avg `0.9881` n `223`; crypto_major avg `-0.102` n `7`; equity avg `0.3191` n `42`; fx avg `0.135` n `4`; index avg `0.0409` n `9`; metal avg `0.1276` n `7`; unknown avg `0.0481` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.413`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3984`, n `159`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `159`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3835`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3786`, n `155`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3634`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3555`, n `155`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3337`, n `159`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3243`, n `159`, moderate_sample_signal
