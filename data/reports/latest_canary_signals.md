# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T18:52:23.901267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.217` n `12`; crypto_alt avg `-0.7026` n `228`; crypto_major avg `-0.6718` n `8`; equity avg `-0.2911` n `69`; fx avg `-0.0047` n `6`; index avg `-0.0702` n `23`; metal avg `-0.118` n `18`; unknown avg `0.7812` n `419`
- 1h: commodity avg `0.2143` n `12`; crypto_alt avg `-1.0143` n `228`; crypto_major avg `-0.8971` n `8`; equity avg `-0.3477` n `69`; fx avg `0.007` n `6`; index avg `-0.0484` n `23`; metal avg `0.0849` n `18`; unknown avg `-0.0839` n `419`
- 4h: commodity avg `-0.2896` n `12`; crypto_alt avg `0.8698` n `228`; crypto_major avg `0.908` n `8`; equity avg `0.6109` n `69`; fx avg `0.0486` n `6`; index avg `0.1087` n `23`; metal avg `-0.203` n `18`; unknown avg `0.9297` n `418`
- 24h: commodity avg `-0.7904` n `12`; crypto_alt avg `-0.0542` n `228`; crypto_major avg `0.2985` n `8`; equity avg `0.9237` n `69`; fx avg `0.2029` n `6`; index avg `-0.099` n `23`; metal avg `0.1558` n `18`; unknown avg `1.7378` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
