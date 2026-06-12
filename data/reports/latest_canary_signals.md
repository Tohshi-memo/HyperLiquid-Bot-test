# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T09:22:28.363723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2148` n `12`; crypto_alt avg `0.3117` n `228`; crypto_major avg `0.2783` n `8`; equity avg `0.2057` n `74`; fx avg `-0.0111` n `6`; index avg `0.1419` n `23`; metal avg `0.1086` n `18`; unknown avg `0.2051` n `643`
- 1h: commodity avg `0.2334` n `12`; crypto_alt avg `0.5605` n `228`; crypto_major avg `0.3446` n `8`; equity avg `0.0606` n `74`; fx avg `0.0001` n `6`; index avg `0.0701` n `23`; metal avg `-0.0202` n `18`; unknown avg `3.6715` n `643`
- 4h: commodity avg `-1.0757` n `12`; crypto_alt avg `0.6177` n `228`; crypto_major avg `0.3084` n `8`; equity avg `-0.0877` n `74`; fx avg `-0.04` n `6`; index avg `-0.0518` n `23`; metal avg `0.463` n `18`; unknown avg `0.1391` n `515`
- 24h: commodity avg `-2.563` n `12`; crypto_alt avg `2.2637` n `228`; crypto_major avg `2.2092` n `8`; equity avg `2.9112` n `74`; fx avg `-0.0402` n `6`; index avg `1.5658` n `23`; metal avg `3.3494` n `18`; unknown avg `-0.3469` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
