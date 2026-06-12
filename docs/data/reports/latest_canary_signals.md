# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T04:22:41.313481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.1706` n `228`; crypto_major avg `0.2303` n `8`; equity avg `0.074` n `74`; fx avg `0.0034` n `6`; index avg `0.0851` n `23`; metal avg `-0.0259` n `18`; unknown avg `2.0379` n `557`
- 1h: commodity avg `-0.4757` n `12`; crypto_alt avg `0.1583` n `228`; crypto_major avg `0.2192` n `8`; equity avg `0.0875` n `74`; fx avg `0.0268` n `6`; index avg `0.2013` n `23`; metal avg `-0.2381` n `18`; unknown avg `4.6339` n `557`
- 4h: commodity avg `-0.0689` n `12`; crypto_alt avg `-0.0186` n `228`; crypto_major avg `0.1642` n `8`; equity avg `-0.1648` n `74`; fx avg `0.0152` n `6`; index avg `-0.0453` n `23`; metal avg `-0.1667` n `18`; unknown avg `2.3829` n `556`
- 24h: commodity avg `-2.6807` n `12`; crypto_alt avg `2.0136` n `228`; crypto_major avg `2.5181` n `8`; equity avg `3.8022` n `74`; fx avg `0.0309` n `6`; index avg `2.001` n `23`; metal avg `3.0672` n `18`; unknown avg `2.3477` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
