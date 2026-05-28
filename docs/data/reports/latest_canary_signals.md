# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T21:37:21.438316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.0045` n `228`; crypto_major avg `0.0495` n `8`; equity avg `0.0136` n `69`; fx avg `-0.0144` n `6`; index avg `0.0241` n `23`; metal avg `-0.0025` n `18`; unknown avg `-0.0395` n `417`
- 1h: commodity avg `-0.3151` n `12`; crypto_alt avg `0.278` n `228`; crypto_major avg `0.3113` n `8`; equity avg `0.1146` n `69`; fx avg `-0.0108` n `6`; index avg `0.0249` n `23`; metal avg `-0.0083` n `18`; unknown avg `-0.0278` n `417`
- 4h: commodity avg `-0.0633` n `12`; crypto_alt avg `0.658` n `228`; crypto_major avg `0.6462` n `8`; equity avg `0.6736` n `69`; fx avg `0.0017` n `6`; index avg `-0.1718` n `23`; metal avg `-0.0798` n `18`; unknown avg `0.3735` n `417`
- 24h: commodity avg `0.6907` n `12`; crypto_alt avg `-2.5438` n `228`; crypto_major avg `-0.2927` n `8`; equity avg `1.7971` n `69`; fx avg `-0.0333` n `6`; index avg `0.6841` n `23`; metal avg `0.5415` n `18`; unknown avg `-0.3897` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
