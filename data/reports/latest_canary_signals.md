# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T17:15:18.859820+00:00`
- Correlation status: `ready`
- Asset price records: `188`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `7`; crypto_alt avg `0.1487` n `223`; crypto_major avg `0.1166` n `7`; equity avg `0.0065` n `42`; fx avg `-0.0021` n `4`; index avg `0.0141` n `9`; metal avg `0.0517` n `7`; unknown avg `0.0259` n `313`
- 1h: commodity avg `0.1094` n `7`; crypto_alt avg `0.1479` n `223`; crypto_major avg `0.1062` n `7`; equity avg `-0.0015` n `42`; fx avg `-0.0048` n `4`; index avg `0.0082` n `9`; metal avg `0.0806` n `7`; unknown avg `0.1883` n `313`
- 4h: commodity avg `-0.2727` n `7`; crypto_alt avg `-0.1037` n `223`; crypto_major avg `-0.0933` n `7`; equity avg `0.1655` n `42`; fx avg `0.0107` n `4`; index avg `0.0384` n `9`; metal avg `0.1991` n `7`; unknown avg `0.1073` n `313`
- 24h: commodity avg `-0.4855` n `7`; crypto_alt avg `-0.2171` n `223`; crypto_major avg `0.0189` n `7`; equity avg `0.524` n `42`; fx avg `0.0787` n `4`; index avg `0.0946` n `9`; metal avg `0.3709` n `7`; unknown avg `0.0683` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4009`, n `184`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3864`, n `180`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3831`, n `184`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3802`, n `180`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.38`, n `184`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3663`, n `184`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3256`, n `184`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3094`, n `180`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3069`, n `184`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3064`, n `184`, moderate_sample_signal
