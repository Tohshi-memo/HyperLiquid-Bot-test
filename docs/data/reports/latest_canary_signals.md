# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T16:07:19.704969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.0135` n `228`; crypto_major avg `0.0273` n `8`; equity avg `0.0814` n `67`; fx avg `-0.0016` n `6`; index avg `0.0707` n `23`; metal avg `-0.043` n `18`; unknown avg `-0.073` n `418`
- 1h: commodity avg `-0.1947` n `12`; crypto_alt avg `-0.4006` n `228`; crypto_major avg `-0.5239` n `8`; equity avg `-0.0564` n `67`; fx avg `-0.002` n `6`; index avg `-0.0783` n `23`; metal avg `-0.1111` n `18`; unknown avg `-0.0957` n `418`
- 4h: commodity avg `0.6961` n `12`; crypto_alt avg `-0.8335` n `228`; crypto_major avg `-0.6753` n `8`; equity avg `-0.1477` n `67`; fx avg `-0.0222` n `6`; index avg `0.2679` n `23`; metal avg `-0.2983` n `18`; unknown avg `-0.0768` n `415`
- 24h: commodity avg `0.8428` n `12`; crypto_alt avg `-1.1782` n `228`; crypto_major avg `-1.1557` n `8`; equity avg `-0.5223` n `67`; fx avg `-0.122` n `6`; index avg `0.2959` n `23`; metal avg `-1.2389` n `18`; unknown avg `-0.5898` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
