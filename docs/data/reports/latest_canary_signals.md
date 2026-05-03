# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T10:00:28.205488+00:00`
- Correlation status: `ready`
- Asset price records: `159`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `7`; crypto_alt avg `0.0348` n `223`; crypto_major avg `-0.0537` n `7`; equity avg `-0.0156` n `42`; fx avg `0.0` n `4`; index avg `0.0001` n `9`; metal avg `-0.0011` n `7`; unknown avg `-0.0046` n `313`
- 1h: commodity avg `-0.0357` n `7`; crypto_alt avg `0.1353` n `223`; crypto_major avg `0.1646` n `7`; equity avg `0.0616` n `42`; fx avg `-0.0021` n `4`; index avg `0.0205` n `9`; metal avg `0.024` n `7`; unknown avg `-0.068` n `313`
- 4h: commodity avg `-0.0836` n `7`; crypto_alt avg `0.5799` n `223`; crypto_major avg `0.3999` n `7`; equity avg `-0.2019` n `42`; fx avg `0.0183` n `4`; index avg `0.0043` n `9`; metal avg `0.1166` n `7`; unknown avg `0.128` n `313`
- 24h: commodity avg `-0.2333` n `7`; crypto_alt avg `1.2209` n `223`; crypto_major avg `0.0225` n `7`; equity avg `0.2525` n `42`; fx avg `0.1327` n `4`; index avg `0.0674` n `9`; metal avg `0.1128` n `7`; unknown avg `0.1247` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4151`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4004`, n `155`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3883`, n `151`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `155`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3831`, n `151`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3732`, n `151`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3658`, n `151`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3352`, n `155`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3279`, n `155`, moderate_sample_signal
