# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T10:52:27.720329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `0.0046` n `228`; crypto_major avg `0.0677` n `8`; equity avg `0.0174` n `78`; fx avg `-0.0001` n `6`; index avg `0.0037` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.0253` n `687`
- 1h: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.297` n `228`; crypto_major avg `-0.0704` n `8`; equity avg `-0.0372` n `78`; fx avg `0.0117` n `6`; index avg `-0.0224` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.0965` n `687`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `-0.1036` n `228`; crypto_major avg `-0.1289` n `8`; equity avg `-0.2057` n `78`; fx avg `0.019` n `6`; index avg `-0.0397` n `23`; metal avg `0.0052` n `18`; unknown avg `-0.2151` n `687`
- 24h: commodity avg `0.4772` n `12`; crypto_alt avg `-3.0652` n `228`; crypto_major avg `-3.3369` n `8`; equity avg `1.1877` n `78`; fx avg `-0.0809` n `6`; index avg `0.2844` n `23`; metal avg `-4.101` n `18`; unknown avg `-0.0186` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
