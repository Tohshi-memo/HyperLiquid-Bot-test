# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T19:22:20.272156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0389` n `12`; crypto_alt avg `-0.0426` n `228`; crypto_major avg `-0.0714` n `8`; equity avg `-0.1146` n `69`; fx avg `-0.0097` n `6`; index avg `-0.0773` n `23`; metal avg `-0.0249` n `18`; unknown avg `0.0633` n `417`
- 1h: commodity avg `0.2502` n `12`; crypto_alt avg `-0.3918` n `228`; crypto_major avg `-0.2563` n `8`; equity avg `-0.2659` n `69`; fx avg `-0.0102` n `6`; index avg `-0.119` n `23`; metal avg `-0.1558` n `18`; unknown avg `0.1035` n `417`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `2.2279` n `228`; crypto_major avg `1.9444` n `8`; equity avg `0.6759` n `69`; fx avg `-0.0158` n `6`; index avg `0.2311` n `23`; metal avg `0.6793` n `18`; unknown avg `0.426` n `417`
- 24h: commodity avg `1.103` n `12`; crypto_alt avg `-3.5334` n `228`; crypto_major avg `-1.0334` n `8`; equity avg `1.5806` n `69`; fx avg `-0.0305` n `6`; index avg `0.8786` n `23`; metal avg `0.5654` n `18`; unknown avg `-0.6903` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
