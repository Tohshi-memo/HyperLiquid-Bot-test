# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T00:22:26.853061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.157` n `239`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0096` n `168`; fx avg `0.0019` n `6`; index avg `0.0023` n `27`; metal avg `-0.0186` n `20`; unknown avg `-0.042` n `1263`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.2054` n `239`; crypto_major avg `0.3232` n `8`; equity avg `0.1563` n `168`; fx avg `-0.004` n `6`; index avg `0.0382` n `27`; metal avg `0.0043` n `20`; unknown avg `4.4869` n `1249`
- 4h: commodity avg `0.0224` n `13`; crypto_alt avg `0.3147` n `239`; crypto_major avg `-0.0659` n `8`; equity avg `0.1148` n `168`; fx avg `-0.0088` n `6`; index avg `0.0435` n `27`; metal avg `0.0304` n `20`; unknown avg `0.2738` n `1163`
- 24h: commodity avg `-0.5388` n `13`; crypto_alt avg `0.2941` n `239`; crypto_major avg `0.2227` n `8`; equity avg `3.5565` n `168`; fx avg `-0.1731` n `6`; index avg `0.3639` n `27`; metal avg `1.003` n `20`; unknown avg `213.094` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
