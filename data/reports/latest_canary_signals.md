# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T16:30:23.088005+00:00`
- Correlation status: `ready`
- Asset price records: `89`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `7`; crypto_alt avg `-0.0401` n `223`; crypto_major avg `-0.0478` n `7`; equity avg `-0.0083` n `42`; fx avg `0.0` n `4`; index avg `0.0` n `9`; metal avg `0.0001` n `7`; unknown avg `0.0226` n `313`
- 1h: commodity avg `-0.0093` n `7`; crypto_alt avg `0.2153` n `223`; crypto_major avg `0.0504` n `7`; equity avg `0.0527` n `42`; fx avg `0.0106` n `4`; index avg `0.0137` n `9`; metal avg `-0.0024` n `7`; unknown avg `0.0` n `313`
- 4h: commodity avg `-0.0246` n `7`; crypto_alt avg `1.0647` n `223`; crypto_major avg `0.2697` n `7`; equity avg `0.0719` n `42`; fx avg `0.0482` n `4`; index avg `0.0008` n `9`; metal avg `-0.0086` n `7`; unknown avg `-0.0608` n `313`
- 24h: commodity avg `0.6258` n `7`; crypto_alt avg `1.1635` n `223`; crypto_major avg `0.1103` n `7`; equity avg `0.3307` n `42`; fx avg `-0.0866` n `4`; index avg `0.1861` n `9`; metal avg `-0.664` n `7`; unknown avg `0.5712` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5281`, n `85`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5246`, n `81`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5098`, n `85`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5001`, n `81`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4758`, n `81`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4746`, n `81`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4613`, n `81`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4537`, n `85`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4278`, n `81`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4267`, n `85`, moderate_sample_signal
