# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T17:22:29.431915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0299` n `233`; crypto_major avg `-0.0667` n `8`; equity avg `-0.0294` n `136`; fx avg `-0.0001` n `6`; index avg `-0.0012` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.084` n `838`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1326` n `233`; crypto_major avg `-0.0729` n `8`; equity avg `-0.029` n `136`; fx avg `0.002` n `6`; index avg `-0.0074` n `26`; metal avg `0.0093` n `20`; unknown avg `0.3041` n `790`
- 4h: commodity avg `0.008` n `12`; crypto_alt avg `0.3352` n `233`; crypto_major avg `-0.0605` n `8`; equity avg `0.021` n `136`; fx avg `-0.0069` n `6`; index avg `0.0069` n `26`; metal avg `0.0251` n `20`; unknown avg `0.0636` n `790`
- 24h: commodity avg `-0.0788` n `12`; crypto_alt avg `0.4994` n `233`; crypto_major avg `-0.5545` n `8`; equity avg `-0.3523` n `136`; fx avg `-0.0134` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0648` n `20`; unknown avg `0.9963` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
