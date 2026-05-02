# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T22:30:22.968307+00:00`
- Correlation status: `ready`
- Asset price records: `113`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `7`; crypto_alt avg `-0.0326` n `223`; crypto_major avg `-0.0031` n `7`; equity avg `-0.0304` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0077` n `9`; metal avg `0.0048` n `7`; unknown avg `-0.0319` n `313`
- 1h: commodity avg `-0.0315` n `7`; crypto_alt avg `-0.184` n `223`; crypto_major avg `0.0321` n `7`; equity avg `-0.0401` n `42`; fx avg `0.0021` n `4`; index avg `-0.0101` n `9`; metal avg `0.0136` n `7`; unknown avg `-0.039` n `313`
- 4h: commodity avg `-0.0388` n `7`; crypto_alt avg `0.2511` n `223`; crypto_major avg `0.0181` n `7`; equity avg `0.289` n `42`; fx avg `0.043` n `4`; index avg `0.0044` n `9`; metal avg `0.0014` n `7`; unknown avg `0.1434` n `313`
- 24h: commodity avg `-0.175` n `7`; crypto_alt avg `1.7046` n `223`; crypto_major avg `0.3756` n `7`; equity avg `0.7633` n `42`; fx avg `0.0558` n `4`; index avg `-0.0583` n `9`; metal avg `0.0225` n `7`; unknown avg `0.2502` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5133`, n `105`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4915`, n `109`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.484`, n `105`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4743`, n `109`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4313`, n `105`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4216`, n `105`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4182`, n `105`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4178`, n `105`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4161`, n `105`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `109`, moderate_sample_signal
