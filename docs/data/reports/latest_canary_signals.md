# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T20:00:24.694291+00:00`
- Correlation status: `ready`
- Asset price records: `199`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `7`; crypto_alt avg `-0.1071` n `223`; crypto_major avg `-0.0498` n `7`; equity avg `-0.0196` n `42`; fx avg `-0.0103` n `4`; index avg `-0.0047` n `9`; metal avg `0.0325` n `7`; unknown avg `-0.0744` n `314`
- 1h: commodity avg `-0.0766` n `7`; crypto_alt avg `0.0745` n `223`; crypto_major avg `0.1215` n `7`; equity avg `0.0022` n `42`; fx avg `0.0179` n `4`; index avg `0.0132` n `9`; metal avg `0.0837` n `7`; unknown avg `-0.07` n `314`
- 4h: commodity avg `0.3203` n `7`; crypto_alt avg `0.321` n `223`; crypto_major avg `0.2565` n `7`; equity avg `0.2543` n `42`; fx avg `-0.0206` n `4`; index avg `0.0527` n `9`; metal avg `0.1676` n `7`; unknown avg `0.2052` n `313`
- 24h: commodity avg `-0.0712` n `7`; crypto_alt avg `-0.2259` n `223`; crypto_major avg `0.1738` n `7`; equity avg `0.3663` n `42`; fx avg `0.0541` n `4`; index avg `0.0597` n `9`; metal avg `0.497` n `7`; unknown avg `0.0707` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3987`, n `195`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3809`, n `195`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3789`, n `191`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3719`, n `195`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3717`, n `191`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3588`, n `195`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3325`, n `195`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.314`, n `195`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3057`, n `195`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.251`, n `191`, moderate_sample_signal
