# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T20:46:15.918286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.128` n `234`; crypto_major avg `-0.0204` n `8`; equity avg `-0.0789` n `142`; fx avg `-0.0022` n `6`; index avg `-0.0176` n `26`; metal avg `0.0129` n `20`; unknown avg `0.0646` n `975`
- 1h: commodity avg `-0.0497` n `12`; crypto_alt avg `0.4169` n `234`; crypto_major avg `0.5337` n `8`; equity avg `0.0083` n `142`; fx avg `0.0172` n `6`; index avg `-0.0079` n `26`; metal avg `0.029` n `20`; unknown avg `0.0641` n `889`
- 4h: commodity avg `-0.1368` n `12`; crypto_alt avg `-1.4614` n `234`; crypto_major avg `-0.7011` n `8`; equity avg `-0.1712` n `142`; fx avg `0.0069` n `6`; index avg `-0.0963` n `26`; metal avg `0.0536` n `20`; unknown avg `2.4322` n `889`
- 24h: commodity avg `0.3156` n `12`; crypto_alt avg `-0.0788` n `234`; crypto_major avg `0.6388` n `8`; equity avg `-0.2955` n `142`; fx avg `0.0777` n `6`; index avg `-0.0426` n `26`; metal avg `-0.2113` n `20`; unknown avg `790.5668` n `786`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
