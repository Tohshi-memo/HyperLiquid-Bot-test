# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T00:07:35.951350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `0.0693` n `239`; crypto_major avg `0.1842` n `8`; equity avg `0.0573` n `168`; fx avg `0.0023` n `6`; index avg `0.0229` n `27`; metal avg `0.0154` n `20`; unknown avg `0.3513` n `1243`
- 1h: commodity avg `-0.0219` n `13`; crypto_alt avg `0.1926` n `239`; crypto_major avg `0.1483` n `8`; equity avg `0.1587` n `168`; fx avg `-0.0073` n `6`; index avg `0.0307` n `27`; metal avg `0.0172` n `20`; unknown avg `2.4926` n `1241`
- 4h: commodity avg `0.0135` n `13`; crypto_alt avg `0.4381` n `239`; crypto_major avg `-0.0367` n `8`; equity avg `0.1645` n `168`; fx avg `-0.0091` n `6`; index avg `0.0463` n `27`; metal avg `0.0681` n `20`; unknown avg `0.4274` n `1159`
- 24h: commodity avg `-0.525` n `13`; crypto_alt avg `0.6214` n `239`; crypto_major avg `0.3754` n `8`; equity avg `3.3949` n `168`; fx avg `-0.2067` n `6`; index avg `0.3196` n `27`; metal avg `1.0266` n `20`; unknown avg `212.2778` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
