# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T19:37:29.839162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `0.1067` n `230`; crypto_major avg `0.1359` n `8`; equity avg `0.2177` n `100`; fx avg `0.0105` n `6`; index avg `0.021` n `25`; metal avg `0.0017` n `20`; unknown avg `0.0962` n `772`
- 1h: commodity avg `-0.0721` n `12`; crypto_alt avg `-0.087` n `230`; crypto_major avg `-0.0614` n `8`; equity avg `-0.021` n `100`; fx avg `0.0137` n `6`; index avg `0.0097` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0672` n `772`
- 4h: commodity avg `-0.1692` n `12`; crypto_alt avg `-0.4475` n `230`; crypto_major avg `-0.4516` n `8`; equity avg `0.3009` n `100`; fx avg `0.0225` n `6`; index avg `0.0892` n `25`; metal avg `-0.023` n `20`; unknown avg `-0.4396` n `772`
- 24h: commodity avg `0.811` n `12`; crypto_alt avg `-1.4128` n `230`; crypto_major avg `-2.0175` n `8`; equity avg `-1.2355` n `99`; fx avg `-0.0679` n `6`; index avg `-0.316` n `25`; metal avg `-0.8142` n `20`; unknown avg `-0.3598` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
