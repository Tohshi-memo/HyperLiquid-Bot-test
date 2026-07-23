# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T18:52:50.419404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0553` n `230`; crypto_major avg `-0.049` n `8`; equity avg `-0.0045` n `100`; fx avg `-0.0005` n `6`; index avg `-0.0102` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0871` n `772`
- 1h: commodity avg `-0.1685` n `12`; crypto_alt avg `-0.2285` n `230`; crypto_major avg `-0.062` n `8`; equity avg `-0.2868` n `100`; fx avg `0.0004` n `6`; index avg `-0.0336` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.2143` n `772`
- 4h: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.7099` n `230`; crypto_major avg `-0.6999` n `8`; equity avg `-0.2002` n `100`; fx avg `0.0094` n `6`; index avg `-0.0179` n `25`; metal avg `-0.1382` n `20`; unknown avg `-0.5634` n `772`
- 24h: commodity avg `0.8563` n `12`; crypto_alt avg `-1.5301` n `230`; crypto_major avg `-2.1141` n `8`; equity avg `-1.1795` n `99`; fx avg `-0.088` n `6`; index avg `-0.3485` n `25`; metal avg `-0.8238` n `20`; unknown avg `-0.5799` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
