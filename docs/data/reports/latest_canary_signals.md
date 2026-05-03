# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T19:30:21.277728+00:00`
- Correlation status: `ready`
- Asset price records: `197`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0392` n `7`; crypto_alt avg `-0.0217` n `223`; crypto_major avg `0.0123` n `7`; equity avg `-0.004` n `42`; fx avg `0.0207` n `4`; index avg `0.0089` n `9`; metal avg `0.0445` n `7`; unknown avg `0.0066` n `314`
- 1h: commodity avg `-0.0361` n `7`; crypto_alt avg `0.03` n `223`; crypto_major avg `0.0192` n `7`; equity avg `0.0469` n `42`; fx avg `0.0303` n `4`; index avg `0.0187` n `9`; metal avg `-0.029` n `7`; unknown avg `0.0678` n `314`
- 4h: commodity avg `0.2063` n `7`; crypto_alt avg `0.0889` n `223`; crypto_major avg `0.0246` n `7`; equity avg `0.2639` n `42`; fx avg `-0.014` n `4`; index avg `0.0569` n `9`; metal avg `0.2255` n `7`; unknown avg `0.0663` n `313`
- 24h: commodity avg `-0.0818` n `7`; crypto_alt avg `-0.2566` n `223`; crypto_major avg `-0.0188` n `7`; equity avg `0.3368` n `42`; fx avg `0.0623` n `4`; index avg `0.0573` n `9`; metal avg `0.4992` n `7`; unknown avg `0.0757` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3991`, n `193`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3812`, n `193`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3764`, n `189`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3763`, n `193`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3691`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3629`, n `193`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.328`, n `193`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3089`, n `193`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.305`, n `193`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2564`, n `189`, moderate_sample_signal
