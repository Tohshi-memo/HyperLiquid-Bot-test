# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T00:03:51.587415+00:00`
- Correlation status: `ready`
- Asset price records: `119`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `7`; crypto_alt avg `-0.1531` n `223`; crypto_major avg `-0.0768` n `7`; equity avg `-0.0452` n `42`; fx avg `0.0043` n `4`; index avg `0.0005` n `9`; metal avg `0.014` n `7`; unknown avg `0.2366` n `313`
- 1h: commodity avg `0.0081` n `7`; crypto_alt avg `-0.0165` n `223`; crypto_major avg `-0.0466` n `7`; equity avg `-0.0082` n `42`; fx avg `0.0083` n `4`; index avg `0.0086` n `9`; metal avg `0.0222` n `7`; unknown avg `0.1139` n `313`
- 4h: commodity avg `0.0727` n `7`; crypto_alt avg `-0.0655` n `223`; crypto_major avg `-0.0336` n `7`; equity avg `0.2221` n `42`; fx avg `0.0362` n `4`; index avg `-0.0163` n `9`; metal avg `0.026` n `7`; unknown avg `0.3019` n `313`
- 24h: commodity avg `-0.1893` n `7`; crypto_alt avg `2.0601` n `223`; crypto_major avg `0.475` n `7`; equity avg `0.8068` n `42`; fx avg `0.0022` n `4`; index avg `0.0328` n `9`; metal avg `0.051` n `7`; unknown avg `0.5715` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4845`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4677`, n `115`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4423`, n `111`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4167`, n `111`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4146`, n `111`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.407`, n `111`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4017`, n `111`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3822`, n `111`, moderate_sample_signal
