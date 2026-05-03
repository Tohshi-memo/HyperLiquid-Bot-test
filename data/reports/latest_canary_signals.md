# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:05:38.458926+00:00`
- Correlation status: `ready`
- Asset price records: `163`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `7`; crypto_alt avg `-0.2574` n `223`; crypto_major avg `-0.1718` n `7`; equity avg `0.0762` n `42`; fx avg `0.005` n `4`; index avg `-0.0457` n `9`; metal avg `0.0027` n `7`; unknown avg `-0.1516` n `313`
- 1h: commodity avg `-0.0299` n `7`; crypto_alt avg `-0.2833` n `223`; crypto_major avg `-0.236` n `7`; equity avg `0.14` n `42`; fx avg `0.0098` n `4`; index avg `-0.0176` n `9`; metal avg `0.0144` n `7`; unknown avg `-0.1847` n `313`
- 4h: commodity avg `-0.0372` n `7`; crypto_alt avg `0.1181` n `223`; crypto_major avg `0.0971` n `7`; equity avg `0.1056` n `42`; fx avg `0.0252` n `4`; index avg `-0.0124` n `9`; metal avg `0.1162` n `7`; unknown avg `-0.2693` n `313`
- 24h: commodity avg `-0.291` n `7`; crypto_alt avg `1.0944` n `223`; crypto_major avg `-0.0533` n `7`; equity avg `0.3529` n `42`; fx avg `0.1398` n `4`; index avg `0.0396` n `9`; metal avg `0.1225` n `7`; unknown avg `-0.0046` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4138`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3992`, n `159`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `159`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3835`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3786`, n `155`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3644`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3567`, n `155`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3352`, n `159`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.324`, n `159`, moderate_sample_signal
