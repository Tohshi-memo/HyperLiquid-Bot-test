# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T02:07:27.264941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.1201` n `234`; crypto_major avg `-0.0417` n `8`; equity avg `0.0481` n `142`; fx avg `-0.023` n `6`; index avg `0.0177` n `26`; metal avg `-0.0687` n `20`; unknown avg `-0.0323` n `972`
- 1h: commodity avg `-0.2443` n `13`; crypto_alt avg `-0.4676` n `234`; crypto_major avg `-0.1051` n `8`; equity avg `0.0508` n `142`; fx avg `0.0009` n `6`; index avg `0.0151` n `26`; metal avg `-0.0072` n `20`; unknown avg `-0.0222` n `972`
- 4h: commodity avg `-0.2884` n `13`; crypto_alt avg `0.6599` n `234`; crypto_major avg `0.0472` n `8`; equity avg `0.3618` n `142`; fx avg `0.1039` n `6`; index avg `0.1251` n `26`; metal avg `-0.0426` n `20`; unknown avg `1.1356` n `942`
- 24h: commodity avg `-0.1136` n `13`; crypto_alt avg `-0.2495` n `234`; crypto_major avg `0.3174` n `8`; equity avg `-0.1547` n `142`; fx avg `0.2105` n `6`; index avg `0.0704` n `26`; metal avg `-0.1754` n `20`; unknown avg `777.409` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
