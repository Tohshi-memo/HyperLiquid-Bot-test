# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T21:27:27.780846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3677` n `12`; crypto_alt avg `0.3288` n `228`; crypto_major avg `0.4092` n `8`; equity avg `0.0607` n `69`; fx avg `-0.0004` n `6`; index avg `-0.0136` n `23`; metal avg `0.0165` n `18`; unknown avg `0.0868` n `417`
- 1h: commodity avg `-0.3264` n `12`; crypto_alt avg `0.4036` n `228`; crypto_major avg `0.3827` n `8`; equity avg `0.1194` n `69`; fx avg `0.0082` n `6`; index avg `-0.0216` n `23`; metal avg `-0.0172` n `18`; unknown avg `0.0101` n `417`
- 4h: commodity avg `-0.1018` n `12`; crypto_alt avg `0.8693` n `228`; crypto_major avg `0.8006` n `8`; equity avg `0.7514` n `69`; fx avg `0.0083` n `6`; index avg `-0.1513` n `23`; metal avg `-0.0548` n `18`; unknown avg `0.4703` n `417`
- 24h: commodity avg `0.7168` n `12`; crypto_alt avg `-3.1855` n `228`; crypto_major avg `-0.781` n `8`; equity avg `1.7534` n `69`; fx avg `0.0006` n `6`; index avg `0.6631` n `23`; metal avg `0.4973` n `18`; unknown avg `-0.5324` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
