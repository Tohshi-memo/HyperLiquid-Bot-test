# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T11:22:25.933273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `-0.0533` n `230`; crypto_major avg `-0.0563` n `8`; equity avg `-0.2457` n `96`; fx avg `0.0127` n `6`; index avg `-0.0543` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.1626` n `769`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.1705` n `230`; crypto_major avg `-0.1311` n `8`; equity avg `-0.105` n `96`; fx avg `-0.0143` n `6`; index avg `-0.0052` n `25`; metal avg `-0.1004` n `20`; unknown avg `0.063` n `769`
- 4h: commodity avg `0.229` n `12`; crypto_alt avg `0.2859` n `230`; crypto_major avg `0.3861` n `8`; equity avg `0.531` n `96`; fx avg `0.0228` n `6`; index avg `0.0483` n `25`; metal avg `0.0238` n `20`; unknown avg `0.1805` n `768`
- 24h: commodity avg `0.125` n `12`; crypto_alt avg `-1.4302` n `230`; crypto_major avg `-2.5523` n `8`; equity avg `-4.3819` n `94`; fx avg `-0.0068` n `6`; index avg `-0.5913` n `25`; metal avg `-0.7015` n `20`; unknown avg `-0.4016` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
