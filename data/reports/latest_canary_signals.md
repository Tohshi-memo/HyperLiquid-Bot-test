# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T08:07:34.255387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.3942` n `234`; crypto_major avg `-0.3348` n `8`; equity avg `-0.0359` n `142`; fx avg `0.0253` n `6`; index avg `0.0011` n `26`; metal avg `-0.0255` n `20`; unknown avg `2.4478` n `945`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `0.463` n `234`; crypto_major avg `0.313` n `8`; equity avg `0.1857` n `142`; fx avg `-0.0173` n `6`; index avg `0.0448` n `26`; metal avg `0.018` n `20`; unknown avg `3.1244` n `945`
- 4h: commodity avg `-0.1085` n `12`; crypto_alt avg `0.047` n `234`; crypto_major avg `-0.2341` n `8`; equity avg `0.1599` n `142`; fx avg `0.0319` n `6`; index avg `0.0609` n `26`; metal avg `0.1878` n `20`; unknown avg `1.4617` n `915`
- 24h: commodity avg `-0.884` n `12`; crypto_alt avg `-0.2275` n `234`; crypto_major avg `-1.1556` n `8`; equity avg `0.5019` n `142`; fx avg `-0.0863` n `6`; index avg `0.133` n `26`; metal avg `0.3896` n `20`; unknown avg `2881.1876` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
