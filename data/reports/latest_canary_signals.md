# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T23:07:30.179417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.2487` n `233`; crypto_major avg `-0.3152` n `8`; equity avg `-0.0378` n `136`; fx avg `0.0144` n `6`; index avg `-0.0009` n `26`; metal avg `0.01` n `20`; unknown avg `-0.0378` n `794`
- 1h: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.7137` n `233`; crypto_major avg `-0.7399` n `8`; equity avg `-0.1816` n `136`; fx avg `-0.0008` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0193` n `20`; unknown avg `-0.1169` n `762`
- 4h: commodity avg `0.2286` n `12`; crypto_alt avg `-0.8038` n `233`; crypto_major avg `-0.7446` n `8`; equity avg `-0.4127` n `136`; fx avg `0.0377` n `6`; index avg `0.0026` n `26`; metal avg `-0.0` n `20`; unknown avg `-0.1612` n `716`
- 24h: commodity avg `1.1126` n `12`; crypto_alt avg `-2.1175` n `233`; crypto_major avg `-2.1524` n `8`; equity avg `-2.1331` n `136`; fx avg `0.1532` n `6`; index avg `-0.348` n `26`; metal avg `-1.3088` n `20`; unknown avg `-0.817` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
