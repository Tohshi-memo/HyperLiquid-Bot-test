# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T12:52:15.996618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `0.1024` n `228`; crypto_major avg `0.1349` n `8`; equity avg `0.0184` n `67`; fx avg `-0.0021` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0681` n `18`; unknown avg `0.1632` n `396`
- 1h: commodity avg `0.0414` n `12`; crypto_alt avg `-0.3727` n `228`; crypto_major avg `-0.0832` n `8`; equity avg `0.0571` n `67`; fx avg `0.005` n `6`; index avg `-0.0091` n `23`; metal avg `-0.1308` n `18`; unknown avg `0.2126` n `396`
- 4h: commodity avg `0.1292` n `12`; crypto_alt avg `-0.4395` n `228`; crypto_major avg `0.2285` n `8`; equity avg `0.2396` n `67`; fx avg `-0.0153` n `6`; index avg `-0.0476` n `23`; metal avg `-0.1364` n `18`; unknown avg `-0.4136` n `396`
- 24h: commodity avg `-2.6681` n `12`; crypto_alt avg `3.4146` n `228`; crypto_major avg `4.6938` n `8`; equity avg `2.8071` n `67`; fx avg `0.0579` n `6`; index avg `1.1709` n `23`; metal avg `1.2081` n `18`; unknown avg `1.6931` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
