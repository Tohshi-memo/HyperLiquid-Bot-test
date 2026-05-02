# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T22:45:37.282721+00:00`
- Correlation status: `ready`
- Asset price records: `114`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `7`; crypto_alt avg `0.043` n `223`; crypto_major avg `0.0616` n `7`; equity avg `-0.0372` n `42`; fx avg `-0.0125` n `4`; index avg `0.004` n `9`; metal avg `0.0061` n `7`; unknown avg `0.0152` n `313`
- 1h: commodity avg `0.0161` n `7`; crypto_alt avg `-0.3146` n `223`; crypto_major avg `-0.245` n `7`; equity avg `-0.0757` n `42`; fx avg `-0.0035` n `4`; index avg `-0.0135` n `9`; metal avg `0.0117` n `7`; unknown avg `-0.0418` n `313`
- 4h: commodity avg `-0.014` n `7`; crypto_alt avg `0.2976` n `223`; crypto_major avg `0.1491` n `7`; equity avg `0.3221` n `42`; fx avg `0.0306` n `4`; index avg `0.0064` n `9`; metal avg `-0.0036` n `7`; unknown avg `0.1648` n `313`
- 24h: commodity avg `-0.1574` n `7`; crypto_alt avg `1.8662` n `223`; crypto_major avg `0.564` n `7`; equity avg `0.6892` n `42`; fx avg `0.0356` n `4`; index avg `-0.08` n `9`; metal avg `0.0336` n `7`; unknown avg `0.3026` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.4894`, n `106`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4887`, n `110`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4717`, n `110`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4511`, n `106`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4209`, n `106`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4175`, n `106`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4173`, n `106`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4156`, n `106`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `110`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4018`, n `106`, moderate_sample_signal
