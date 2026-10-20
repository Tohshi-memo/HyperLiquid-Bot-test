# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T06:22:26.484307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1229` n `13`; crypto_alt avg `0.2643` n `237`; crypto_major avg `0.1324` n `8`; equity avg `0.222` n `151`; fx avg `0.0185` n `6`; index avg `0.0519` n `26`; metal avg `0.0599` n `20`; unknown avg `0.2811` n `1198`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.2055` n `237`; crypto_major avg `-0.3318` n `8`; equity avg `0.0003` n `151`; fx avg `0.0032` n `6`; index avg `0.0366` n `26`; metal avg `-0.0194` n `20`; unknown avg `7.315` n `1176`
- 4h: commodity avg `0.05` n `13`; crypto_alt avg `0.2085` n `237`; crypto_major avg `0.0851` n `8`; equity avg `-0.7448` n `151`; fx avg `0.0344` n `6`; index avg `-0.1292` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.9827` n `1168`
- 24h: commodity avg `0.3235` n `13`; crypto_alt avg `-0.0714` n `237`; crypto_major avg `-0.7891` n `8`; equity avg `-1.7592` n `151`; fx avg `0.0193` n `6`; index avg `-0.2683` n `26`; metal avg `-0.2821` n `20`; unknown avg `5.483` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
