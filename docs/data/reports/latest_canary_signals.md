# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T06:22:38.826455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1773` n `12`; crypto_alt avg `-0.0932` n `228`; crypto_major avg `-0.058` n `8`; equity avg `-0.0372` n `74`; fx avg `0.0167` n `6`; index avg `-0.0705` n `23`; metal avg `0.0924` n `18`; unknown avg `-0.0453` n `689`
- 1h: commodity avg `-0.0697` n `12`; crypto_alt avg `0.0979` n `228`; crypto_major avg `-0.0559` n `8`; equity avg `-0.1146` n `74`; fx avg `0.0016` n `6`; index avg `-0.0447` n `23`; metal avg `-0.4101` n `18`; unknown avg `-0.0403` n `529`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.4944` n `228`; crypto_major avg `0.0521` n `8`; equity avg `0.192` n `74`; fx avg `0.0184` n `6`; index avg `0.1664` n `23`; metal avg `-0.4413` n `18`; unknown avg `0.157` n `529`
- 24h: commodity avg `-0.9131` n `12`; crypto_alt avg `2.8211` n `228`; crypto_major avg `2.7726` n `8`; equity avg `1.7516` n `74`; fx avg `0.0475` n `6`; index avg `0.9282` n `23`; metal avg `1.6997` n `18`; unknown avg `3.9765` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
