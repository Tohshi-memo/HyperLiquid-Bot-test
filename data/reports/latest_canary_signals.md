# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T04:45:23.194210+00:00`
- Correlation status: `ready`
- Asset price records: `138`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `7`; crypto_alt avg `0.0922` n `223`; crypto_major avg `-0.0332` n `7`; equity avg `-0.0046` n `42`; fx avg `-0.004` n `4`; index avg `0.0545` n `9`; metal avg `-0.0068` n `7`; unknown avg `0.0219` n `313`
- 1h: commodity avg `0.0229` n `7`; crypto_alt avg `0.2305` n `223`; crypto_major avg `0.0462` n `7`; equity avg `-0.0044` n `42`; fx avg `-0.0035` n `4`; index avg `0.0198` n `9`; metal avg `-0.0039` n `7`; unknown avg `-0.0265` n `313`
- 4h: commodity avg `0.0399` n `7`; crypto_alt avg `-0.7942` n `223`; crypto_major avg `-0.4354` n `7`; equity avg `-0.0611` n `42`; fx avg `-0.0016` n `4`; index avg `-0.0317` n `9`; metal avg `0.0256` n `7`; unknown avg `0.1693` n `313`
- 24h: commodity avg `-0.1099` n `7`; crypto_alt avg `1.1799` n `223`; crypto_major avg `-0.1663` n `7`; equity avg `0.653` n `42`; fx avg `0.0364` n `4`; index avg `0.0453` n `9`; metal avg `0.077` n `7`; unknown avg `0.1143` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4446`, n `134`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4295`, n `134`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4091`, n `130`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.407`, n `130`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4041`, n `134`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3987`, n `130`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3936`, n `130`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3886`, n `130`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3863`, n `134`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3737`, n `130`, moderate_sample_signal
