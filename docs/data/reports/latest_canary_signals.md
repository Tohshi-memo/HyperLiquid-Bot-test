# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T12:58:04.212735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `-0.1492` n `230`; crypto_major avg `-0.0758` n `8`; equity avg `-0.0946` n `98`; fx avg `-0.0049` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0265` n `770`
- 1h: commodity avg `0.401` n `12`; crypto_alt avg `-0.1666` n `230`; crypto_major avg `-0.3876` n `8`; equity avg `-0.2935` n `98`; fx avg `-0.0064` n `6`; index avg `-0.0707` n `25`; metal avg `-0.1753` n `20`; unknown avg `0.0248` n `770`
- 4h: commodity avg `0.1913` n `12`; crypto_alt avg `0.7458` n `230`; crypto_major avg `0.7975` n `8`; equity avg `0.6727` n `98`; fx avg `-0.0359` n `6`; index avg `0.1351` n `25`; metal avg `-0.0515` n `20`; unknown avg `0.1747` n `770`
- 24h: commodity avg `-0.4255` n `12`; crypto_alt avg `0.7734` n `230`; crypto_major avg `0.3437` n `8`; equity avg `0.8129` n `97`; fx avg `-0.0514` n `6`; index avg `0.1682` n `25`; metal avg `0.1603` n `20`; unknown avg `0.055` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1004`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0884`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
