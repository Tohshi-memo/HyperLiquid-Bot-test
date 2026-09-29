# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T21:52:33.951765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.1327` n `234`; crypto_major avg `0.1008` n `8`; equity avg `-0.0084` n `142`; fx avg `0.0019` n `6`; index avg `-0.0016` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.0156` n `938`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `-0.1019` n `234`; crypto_major avg `-0.1256` n `8`; equity avg `0.0259` n `142`; fx avg `0.0013` n `6`; index avg `-0.0133` n `26`; metal avg `0.0085` n `20`; unknown avg `1.3685` n `930`
- 4h: commodity avg `-0.2268` n `12`; crypto_alt avg `1.2456` n `234`; crypto_major avg `0.6836` n `8`; equity avg `0.3276` n `142`; fx avg `0.0098` n `6`; index avg `0.0996` n `26`; metal avg `0.2927` n `20`; unknown avg `3.7124` n `872`
- 24h: commodity avg `-1.0223` n `12`; crypto_alt avg `1.4862` n `234`; crypto_major avg `0.0807` n `8`; equity avg `0.7393` n `142`; fx avg `-0.1637` n `6`; index avg `0.0707` n `26`; metal avg `0.2865` n `20`; unknown avg `3191.1631` n `810`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
