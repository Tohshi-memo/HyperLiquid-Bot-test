# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T15:22:25.280096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.3516` n `228`; crypto_major avg `-0.1263` n `8`; equity avg `-0.0683` n `74`; fx avg `-0.0002` n `6`; index avg `0.0238` n `23`; metal avg `0.0019` n `18`; unknown avg `-0.468` n `515`
- 1h: commodity avg `-0.038` n `12`; crypto_alt avg `-1.2712` n `228`; crypto_major avg `-1.0114` n `8`; equity avg `-0.2296` n `74`; fx avg `-0.0014` n `6`; index avg `-0.0718` n `23`; metal avg `-0.0769` n `18`; unknown avg `-1.8252` n `515`
- 4h: commodity avg `0.0957` n `12`; crypto_alt avg `0.0212` n `228`; crypto_major avg `-0.2392` n `8`; equity avg `0.4447` n `74`; fx avg `0.0078` n `6`; index avg `0.5163` n `23`; metal avg `-0.1535` n `18`; unknown avg `-0.6513` n `411`
- 24h: commodity avg `-0.3338` n `12`; crypto_alt avg `-1.8512` n `228`; crypto_major avg `-1.7197` n `8`; equity avg `-3.3802` n `74`; fx avg `-0.1272` n `6`; index avg `-2.206` n `23`; metal avg `-1.5032` n `18`; unknown avg `0.4363` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
