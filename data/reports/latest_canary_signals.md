# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T01:52:35.085280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1577` n `12`; crypto_alt avg `0.1795` n `228`; crypto_major avg `0.1671` n `8`; equity avg `0.0716` n `74`; fx avg `0.0106` n `6`; index avg `-0.0368` n `23`; metal avg `0.0169` n `18`; unknown avg `-0.1442` n `637`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `0.1791` n `228`; crypto_major avg `0.0468` n `8`; equity avg `0.1283` n `74`; fx avg `0.0497` n `6`; index avg `0.008` n `23`; metal avg `0.2877` n `18`; unknown avg `1.5357` n `637`
- 4h: commodity avg `0.375` n `12`; crypto_alt avg `0.0452` n `228`; crypto_major avg `0.1402` n `8`; equity avg `0.2986` n `74`; fx avg `-0.0062` n `6`; index avg `0.2079` n `23`; metal avg `1.2775` n `18`; unknown avg `-0.0795` n `629`
- 24h: commodity avg `-0.8203` n `12`; crypto_alt avg `1.6603` n `228`; crypto_major avg `2.0461` n `8`; equity avg `1.6556` n `74`; fx avg `0.0398` n `6`; index avg `0.767` n `23`; metal avg `1.9637` n `18`; unknown avg `1.281` n `577`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
