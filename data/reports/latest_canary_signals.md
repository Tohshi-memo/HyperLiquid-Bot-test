# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T21:52:22.041743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1256` n `12`; crypto_alt avg `-0.077` n `228`; crypto_major avg `-0.0285` n `8`; equity avg `0.0585` n `69`; fx avg `-0.0014` n `6`; index avg `-0.0556` n `23`; metal avg `-0.0051` n `18`; unknown avg `-0.0219` n `417`
- 1h: commodity avg `-0.1316` n `12`; crypto_alt avg `0.0447` n `228`; crypto_major avg `0.2188` n `8`; equity avg `0.1347` n `69`; fx avg `-0.013` n `6`; index avg `-0.0217` n `23`; metal avg `0.0035` n `18`; unknown avg `-0.1164` n `417`
- 4h: commodity avg `0.0373` n `12`; crypto_alt avg `0.4075` n `228`; crypto_major avg `0.6071` n `8`; equity avg `0.4935` n `69`; fx avg `-0.0023` n `6`; index avg `-0.2368` n `23`; metal avg `-0.1865` n `18`; unknown avg `0.4677` n `417`
- 24h: commodity avg `0.7485` n `12`; crypto_alt avg `-1.3161` n `228`; crypto_major avg `0.4326` n `8`; equity avg `1.899` n `69`; fx avg `-0.0323` n `6`; index avg `0.6649` n `23`; metal avg `0.5768` n `18`; unknown avg `-0.262` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
