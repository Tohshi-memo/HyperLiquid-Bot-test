# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T05:07:15.893887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `0.2696` n `228`; crypto_major avg `0.2052` n `8`; equity avg `0.037` n `66`; fx avg `-0.0047` n `6`; index avg `0.0732` n `23`; metal avg `0.2101` n `18`; unknown avg `0.0296` n `384`
- 1h: commodity avg `0.1876` n `12`; crypto_alt avg `0.3691` n `228`; crypto_major avg `0.2467` n `8`; equity avg `-0.0098` n `66`; fx avg `0.0075` n `6`; index avg `0.0221` n `23`; metal avg `0.0832` n `18`; unknown avg `-0.1871` n `384`
- 4h: commodity avg `-0.1483` n `12`; crypto_alt avg `0.7233` n `228`; crypto_major avg `0.4126` n `8`; equity avg `0.1499` n `66`; fx avg `-0.001` n `6`; index avg `-0.0697` n `23`; metal avg `-0.1459` n `18`; unknown avg `-0.3274` n `384`
- 24h: commodity avg `0.7333` n `12`; crypto_alt avg `-0.7835` n `228`; crypto_major avg `-0.5319` n `8`; equity avg `0.2176` n `66`; fx avg `-0.1165` n `6`; index avg `-0.4734` n `23`; metal avg `-1.8964` n `18`; unknown avg `0.5641` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
