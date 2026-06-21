# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T10:22:29.714711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.1343` n `228`; crypto_major avg `0.1276` n `8`; equity avg `-0.0063` n `78`; fx avg `-0.0091` n `6`; index avg `-0.0006` n `23`; metal avg `-0.0034` n `18`; unknown avg `-0.0879` n `702`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.5568` n `228`; crypto_major avg `0.4083` n `8`; equity avg `0.0162` n `78`; fx avg `-0.0014` n `6`; index avg `0.0039` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.027` n `702`
- 4h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.8205` n `228`; crypto_major avg `0.1563` n `8`; equity avg `0.0308` n `78`; fx avg `-0.0124` n `6`; index avg `0.0105` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.3249` n `694`
- 24h: commodity avg `0.0816` n `12`; crypto_alt avg `1.4414` n `228`; crypto_major avg `0.18` n `8`; equity avg `0.3472` n `78`; fx avg `0.0228` n `6`; index avg `0.0348` n `23`; metal avg `-0.0025` n `18`; unknown avg `0.0969` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
