# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T17:15:17.296746+00:00`
- Correlation status: `ready`
- Asset price records: `92`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `7`; crypto_alt avg `-0.0184` n `223`; crypto_major avg `-0.0503` n `7`; equity avg `0.0702` n `42`; fx avg `-0.0011` n `4`; index avg `0.0026` n `9`; metal avg `0.003` n `7`; unknown avg `0.0079` n `313`
- 1h: commodity avg `-0.0413` n `7`; crypto_alt avg `0.2778` n `223`; crypto_major avg `0.0142` n `7`; equity avg `0.0621` n `42`; fx avg `0.0359` n `4`; index avg `0.0024` n `9`; metal avg `0.007` n `7`; unknown avg `0.1379` n `313`
- 4h: commodity avg `-0.0613` n `7`; crypto_alt avg `1.416` n `223`; crypto_major avg `0.244` n `7`; equity avg `0.0893` n `42`; fx avg `0.0826` n `4`; index avg `-0.0037` n `9`; metal avg `-0.0149` n `7`; unknown avg `0.1344` n `313`
- 24h: commodity avg `0.5846` n `7`; crypto_alt avg `1.4906` n `223`; crypto_major avg `0.1721` n `7`; equity avg `0.405` n `42`; fx avg `-0.0508` n `4`; index avg `0.1885` n `9`; metal avg `-0.6572` n `7`; unknown avg `0.6412` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5266`, n `88`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5223`, n `84`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5082`, n `88`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4915`, n `84`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.475`, n `84`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4737`, n `84`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4607`, n `84`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4515`, n `88`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4277`, n `88`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4244`, n `84`, moderate_sample_signal
