# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T21:52:31.711664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0508` n `12`; crypto_alt avg `-0.1542` n `228`; crypto_major avg `-0.1457` n `8`; equity avg `-0.0112` n `78`; fx avg `0.0495` n `6`; index avg `-0.0201` n `23`; metal avg `-0.0264` n `18`; unknown avg `-0.1592` n `702`
- 1h: commodity avg `0.1494` n `12`; crypto_alt avg `-0.4734` n `228`; crypto_major avg `-0.2729` n `8`; equity avg `0.0549` n `78`; fx avg `0.0151` n `6`; index avg `-0.0229` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.1807` n `702`
- 4h: commodity avg `0.213` n `12`; crypto_alt avg `-1.0605` n `228`; crypto_major avg `-0.6385` n `8`; equity avg `-0.0986` n `78`; fx avg `-0.0447` n `6`; index avg `-0.0321` n `23`; metal avg `-0.1618` n `18`; unknown avg `0.9745` n `694`
- 24h: commodity avg `0.4003` n `12`; crypto_alt avg `0.2802` n `228`; crypto_major avg `-0.7046` n `8`; equity avg `0.156` n `78`; fx avg `-0.1086` n `6`; index avg `-0.0167` n `23`; metal avg `-0.1599` n `18`; unknown avg `0.7146` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
