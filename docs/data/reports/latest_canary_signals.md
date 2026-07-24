# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T12:22:26.004550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0507` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `0.0705` n `8`; equity avg `0.1351` n `100`; fx avg `-0.001` n `6`; index avg `0.0321` n `25`; metal avg `0.018` n `20`; unknown avg `0.0175` n `773`
- 1h: commodity avg `0.0432` n `12`; crypto_alt avg `-0.0135` n `230`; crypto_major avg `-0.0775` n `8`; equity avg `0.1376` n `100`; fx avg `-0.014` n `6`; index avg `0.0353` n `25`; metal avg `0.0272` n `20`; unknown avg `-0.0402` n `773`
- 4h: commodity avg `-0.0495` n `12`; crypto_alt avg `-0.4697` n `230`; crypto_major avg `-0.5025` n `8`; equity avg `0.294` n `100`; fx avg `-0.0507` n `6`; index avg `0.0998` n `25`; metal avg `0.1784` n `20`; unknown avg `-0.0259` n `772`
- 24h: commodity avg `-0.2781` n `12`; crypto_alt avg `-1.4198` n `230`; crypto_major avg `-1.8444` n `8`; equity avg `-0.8302` n `99`; fx avg `-0.1543` n `6`; index avg `-0.244` n `25`; metal avg `-0.1249` n `20`; unknown avg `0.1207` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0992`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
