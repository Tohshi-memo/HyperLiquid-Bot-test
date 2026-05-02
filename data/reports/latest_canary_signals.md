# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T19:00:28.962247+00:00`
- Correlation status: `ready`
- Asset price records: `99`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `7`; crypto_alt avg `0.0543` n `223`; crypto_major avg `0.1171` n `7`; equity avg `0.0274` n `42`; fx avg `-0.0021` n `4`; index avg `0.007` n `9`; metal avg `-0.0086` n `7`; unknown avg `0.0598` n `313`
- 1h: commodity avg `0.0182` n `7`; crypto_alt avg `0.2547` n `223`; crypto_major avg `0.1614` n `7`; equity avg `-0.0007` n `42`; fx avg `0.0011` n `4`; index avg `0.0268` n `9`; metal avg `-0.0012` n `7`; unknown avg `0.086` n `313`
- 4h: commodity avg `-0.1458` n `7`; crypto_alt avg `0.5373` n `223`; crypto_major avg `0.1712` n `7`; equity avg `0.2049` n `42`; fx avg `0.0484` n `4`; index avg `0.0417` n `9`; metal avg `-0.0226` n `7`; unknown avg `0.1274` n `313`
- 24h: commodity avg `0.0489` n `7`; crypto_alt avg `1.34` n `223`; crypto_major avg `0.2416` n `7`; equity avg `0.7039` n `42`; fx avg `-0.0308` n `4`; index avg `0.0922` n `9`; metal avg `-0.2757` n `7`; unknown avg `0.4647` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5239`, n `91`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5204`, n `95`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5023`, n `95`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4945`, n `91`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4487`, n `91`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4338`, n `91`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4239`, n `91`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4237`, n `95`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4231`, n `91`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4207`, n `91`, moderate_sample_signal
