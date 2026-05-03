# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T02:15:19.001796+00:00`
- Correlation status: `ready`
- Asset price records: `128`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `7`; crypto_alt avg `-0.202` n `223`; crypto_major avg `-0.0124` n `7`; equity avg `-0.0179` n `42`; fx avg `0.0111` n `4`; index avg `-0.0081` n `9`; metal avg `0.016` n `7`; unknown avg `-0.0318` n `313`
- 1h: commodity avg `-0.031` n `7`; crypto_alt avg `-0.6216` n `223`; crypto_major avg `-0.2222` n `7`; equity avg `-0.047` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0402` n `9`; metal avg `0.0123` n `7`; unknown avg `0.0678` n `313`
- 4h: commodity avg `0.0586` n `7`; crypto_alt avg `-1.172` n `223`; crypto_major avg `-0.6613` n `7`; equity avg `-0.0801` n `42`; fx avg `-0.0064` n `4`; index avg `-0.0224` n `9`; metal avg `0.0172` n `7`; unknown avg `-0.118` n `313`
- 24h: commodity avg `-0.1641` n `7`; crypto_alt avg `0.7161` n `223`; crypto_major avg `-0.2391` n `7`; equity avg `0.5828` n `42`; fx avg `-0.0028` n `4`; index avg `0.0202` n `9`; metal avg `0.0367` n `7`; unknown avg `0.0984` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4525`, n `124`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4371`, n `124`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4172`, n `120`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4149`, n `120`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4041`, n `120`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4039`, n `124`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3989`, n `120`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3932`, n `124`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3885`, n `120`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3861`, n `124`, moderate_sample_signal
