# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T15:52:28.447043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0526` n `12`; crypto_alt avg `-0.0201` n `228`; crypto_major avg `0.0098` n `8`; equity avg `-0.0203` n `78`; fx avg `0.0001` n `6`; index avg `-0.0109` n `23`; metal avg `-0.0115` n `18`; unknown avg `-0.0414` n `701`
- 1h: commodity avg `0.0601` n `12`; crypto_alt avg `0.3128` n `228`; crypto_major avg `0.116` n `8`; equity avg `0.0062` n `78`; fx avg `-0.0024` n `6`; index avg `0.0039` n `23`; metal avg `-0.0068` n `18`; unknown avg `0.0436` n `701`
- 4h: commodity avg `0.1595` n `12`; crypto_alt avg `0.2939` n `228`; crypto_major avg `0.0746` n `8`; equity avg `0.0061` n `78`; fx avg `0.0189` n `6`; index avg `-0.0023` n `23`; metal avg `0.0247` n `18`; unknown avg `0.2522` n `573`
- 24h: commodity avg `0.5934` n `12`; crypto_alt avg `-2.7386` n `228`; crypto_major avg `-3.1568` n `8`; equity avg `1.1777` n `78`; fx avg `-0.0588` n `6`; index avg `0.2915` n `23`; metal avg `-4.0751` n `18`; unknown avg `-0.1318` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
