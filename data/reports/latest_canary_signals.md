# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T13:07:38.044031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `0.0239` n `228`; crypto_major avg `-0.0487` n `8`; equity avg `-0.1383` n `77`; fx avg `0.0119` n `6`; index avg `-0.0442` n `23`; metal avg `-0.0761` n `18`; unknown avg `-0.0709` n `687`
- 1h: commodity avg `-0.098` n `12`; crypto_alt avg `-0.0226` n `228`; crypto_major avg `0.2265` n `8`; equity avg `-0.5704` n `77`; fx avg `0.0018` n `6`; index avg `-0.1957` n `23`; metal avg `0.0718` n `18`; unknown avg `0.3515` n `687`
- 4h: commodity avg `-0.3113` n `12`; crypto_alt avg `-0.3921` n `228`; crypto_major avg `0.1533` n `8`; equity avg `-0.7737` n `77`; fx avg `-0.0071` n `6`; index avg `-0.1817` n `23`; metal avg `0.1921` n `18`; unknown avg `0.6147` n `687`
- 24h: commodity avg `-0.4286` n `12`; crypto_alt avg `-0.3656` n `228`; crypto_major avg `1.4482` n `8`; equity avg `1.1465` n `76`; fx avg `-0.0722` n `6`; index avg `0.2915` n `23`; metal avg `0.122` n `18`; unknown avg `0.7437` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
