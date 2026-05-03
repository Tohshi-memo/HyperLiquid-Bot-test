# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T18:45:20.372655+00:00`
- Correlation status: `ready`
- Asset price records: `194`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0528` n `7`; crypto_alt avg `0.0281` n `223`; crypto_major avg `-0.0333` n `7`; equity avg `0.0429` n `42`; fx avg `0.0` n `4`; index avg `0.0018` n `9`; metal avg `-0.0334` n `7`; unknown avg `0.0323` n `314`
- 1h: commodity avg `0.2553` n `7`; crypto_alt avg `0.1068` n `223`; crypto_major avg `-0.1164` n `7`; equity avg `0.0107` n `42`; fx avg `-0.0403` n `4`; index avg `-0.0262` n `9`; metal avg `0.0335` n `7`; unknown avg `0.0006` n `314`
- 4h: commodity avg `-0.0083` n `7`; crypto_alt avg `0.1936` n `223`; crypto_major avg `-0.0301` n `7`; equity avg `0.2305` n `42`; fx avg `-0.0408` n `4`; index avg `0.072` n `9`; metal avg `0.242` n `7`; unknown avg `0.328` n `313`
- 24h: commodity avg `-0.1292` n `7`; crypto_alt avg `-0.0339` n `223`; crypto_major avg `0.0582` n `7`; equity avg `0.5039` n `42`; fx avg `0.0351` n `4`; index avg `0.0593` n `9`; metal avg `0.4797` n `7`; unknown avg `0.0338` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3988`, n `190`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.381`, n `190`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3769`, n `190`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3761`, n `186`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3688`, n `186`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3634`, n `190`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3269`, n `190`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3078`, n `190`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3045`, n `190`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.266`, n `186`, moderate_sample_signal
