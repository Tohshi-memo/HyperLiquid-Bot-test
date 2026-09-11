# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T00:22:31.400522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `0.1519` n `233`; crypto_major avg `0.0386` n `8`; equity avg `-0.0138` n `136`; fx avg `0.0061` n `6`; index avg `0.0079` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.5043` n `796`
- 1h: commodity avg `-0.1365` n `12`; crypto_alt avg `0.3653` n `233`; crypto_major avg `0.0581` n `8`; equity avg `0.0266` n `136`; fx avg `-0.017` n `6`; index avg `0.0106` n `26`; metal avg `0.0048` n `20`; unknown avg `0.185` n `790`
- 4h: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.9097` n `233`; crypto_major avg `-0.9617` n `8`; equity avg `-0.2947` n `136`; fx avg `0.0035` n `6`; index avg `-0.0215` n `26`; metal avg `0.0222` n `20`; unknown avg `0.3366` n `732`
- 24h: commodity avg `1.0939` n `12`; crypto_alt avg `-2.0171` n `233`; crypto_major avg `-2.233` n `8`; equity avg `-2.1606` n `136`; fx avg `0.1249` n `6`; index avg `-0.3721` n `26`; metal avg `-1.2558` n `20`; unknown avg `-0.3928` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
