# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T15:52:25.779047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0454` n `228`; crypto_major avg `-0.0204` n `8`; equity avg `-0.0013` n `78`; fx avg `0.0076` n `6`; index avg `-0.01` n `23`; metal avg `0.0136` n `18`; unknown avg `0.0189` n `702`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `0.2546` n `228`; crypto_major avg `0.2201` n `8`; equity avg `0.1036` n `78`; fx avg `0.0654` n `6`; index avg `-0.0033` n `23`; metal avg `0.0227` n `18`; unknown avg `0.1543` n `702`
- 4h: commodity avg `0.1333` n `12`; crypto_alt avg `0.6662` n `228`; crypto_major avg `0.5088` n `8`; equity avg `0.0496` n `78`; fx avg `0.0304` n `6`; index avg `-0.0202` n `23`; metal avg `0.0068` n `18`; unknown avg `0.3137` n `702`
- 24h: commodity avg `0.0735` n `12`; crypto_alt avg `1.3729` n `228`; crypto_major avg `-0.0768` n `8`; equity avg `0.3647` n `78`; fx avg `0.043` n `6`; index avg `0.0107` n `23`; metal avg `-0.0892` n `18`; unknown avg `0.5948` n `653`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
