# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T10:22:32.016549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.0416` n `234`; crypto_major avg `-0.0473` n `8`; equity avg `-0.0301` n `141`; fx avg `0.0062` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0053` n `20`; unknown avg `1.1383` n `962`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `-0.4777` n `234`; crypto_major avg `-0.1751` n `8`; equity avg `0.0375` n `141`; fx avg `-0.0051` n `6`; index avg `-0.0204` n `26`; metal avg `0.0803` n `20`; unknown avg `25.7343` n `960`
- 4h: commodity avg `0.3153` n `12`; crypto_alt avg `-1.1306` n `234`; crypto_major avg `-0.1258` n `8`; equity avg `-1.0583` n `141`; fx avg `-0.0849` n `6`; index avg `-0.0774` n `26`; metal avg `-0.0984` n `20`; unknown avg `24.4447` n `942`
- 24h: commodity avg `-0.0494` n `12`; crypto_alt avg `-4.4777` n `234`; crypto_major avg `-3.2819` n `8`; equity avg `-2.8842` n `141`; fx avg `0.0268` n `6`; index avg `-0.3007` n `26`; metal avg `-0.9068` n `20`; unknown avg `6.2293` n `814`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
