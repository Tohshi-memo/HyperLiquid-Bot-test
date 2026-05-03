# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T04:00:29.804392+00:00`
- Correlation status: `ready`
- Asset price records: `135`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `7`; crypto_alt avg `-0.0089` n `223`; crypto_major avg `0.0247` n `7`; equity avg `-0.0067` n `42`; fx avg `0.0005` n `4`; index avg `0.0011` n `9`; metal avg `-0.0039` n `7`; unknown avg `-0.037` n `313`
- 1h: commodity avg `0.0724` n `7`; crypto_alt avg `-0.0421` n `223`; crypto_major avg `0.0607` n `7`; equity avg `-0.0024` n `42`; fx avg `0.0026` n `4`; index avg `0.0019` n `9`; metal avg `0.0082` n `7`; unknown avg `-0.0339` n `313`
- 4h: commodity avg `0.0453` n `7`; crypto_alt avg `-1.1979` n `223`; crypto_major avg `-0.6169` n `7`; equity avg `-0.0813` n `42`; fx avg `-0.0027` n `4`; index avg `-0.028` n `9`; metal avg `-0.0016` n `7`; unknown avg `-0.1404` n `313`
- 24h: commodity avg `-0.1138` n `7`; crypto_alt avg `0.6382` n `223`; crypto_major avg `-0.3121` n `7`; equity avg `0.5751` n `42`; fx avg `0.0195` n `4`; index avg `-0.004` n `9`; metal avg `0.0519` n `7`; unknown avg `0.0855` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4473`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4321`, n `131`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4237`, n `131`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4166`, n `131`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.413`, n `127`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4123`, n `131`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4105`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `131`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3987`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3936`, n `127`, moderate_sample_signal
