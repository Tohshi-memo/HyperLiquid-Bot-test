# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T19:37:43.009019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.0154` n `234`; crypto_major avg `-0.097` n `8`; equity avg `-0.0727` n `142`; fx avg `-0.0024` n `6`; index avg `-0.0059` n `26`; metal avg `0.0104` n `20`; unknown avg `188.568` n `962`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `0.2245` n `234`; crypto_major avg `0.0341` n `8`; equity avg `0.0319` n `142`; fx avg `-0.0083` n `6`; index avg `0.0361` n `26`; metal avg `0.0364` n `20`; unknown avg `3.9978` n `960`
- 4h: commodity avg `-0.3932` n `12`; crypto_alt avg `-0.0753` n `234`; crypto_major avg `-0.0012` n `8`; equity avg `-0.0961` n `142`; fx avg `-0.0328` n `6`; index avg `0.0621` n `26`; metal avg `0.2191` n `20`; unknown avg `12.0888` n `954`
- 24h: commodity avg `-0.8407` n `12`; crypto_alt avg `1.5396` n `234`; crypto_major avg `0.1195` n `8`; equity avg `0.5147` n `142`; fx avg `-0.1689` n `6`; index avg `0.0574` n `26`; metal avg `0.0989` n `20`; unknown avg `0.1624` n `826`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
