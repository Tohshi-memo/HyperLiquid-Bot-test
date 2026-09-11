# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T10:38:04.802097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `-0.239` n `233`; crypto_major avg `-0.1045` n `8`; equity avg `-0.0364` n `136`; fx avg `-0.009` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0294` n `20`; unknown avg `-0.0822` n `796`
- 1h: commodity avg `-0.0868` n `12`; crypto_alt avg `-0.3472` n `233`; crypto_major avg `-0.0257` n `8`; equity avg `0.0241` n `136`; fx avg `-0.0174` n `6`; index avg `0.0117` n `26`; metal avg `0.0475` n `20`; unknown avg `-0.1807` n `794`
- 4h: commodity avg `-0.4014` n `12`; crypto_alt avg `-0.7811` n `233`; crypto_major avg `-0.3147` n `8`; equity avg `0.297` n `136`; fx avg `-0.0907` n `6`; index avg `0.0682` n `26`; metal avg `0.0142` n `20`; unknown avg `-0.3926` n `786`
- 24h: commodity avg `0.2913` n `12`; crypto_alt avg `-1.6504` n `233`; crypto_major avg `-1.6` n `8`; equity avg `-0.8839` n `136`; fx avg `-0.0711` n `6`; index avg `-0.1175` n `26`; metal avg `-0.5167` n `20`; unknown avg `1.3581` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
