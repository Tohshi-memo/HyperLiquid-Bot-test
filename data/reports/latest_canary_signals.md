# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T09:22:16.178242+00:00`
- Correlation status: `ready`
- Asset price records: `537`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0858` n `12`; crypto_alt avg `0.1019` n `228`; crypto_major avg `-0.0022` n `8`; equity avg `0.37` n `65`; fx avg `-0.0057` n `4`; index avg `0.0562` n `23`; metal avg `0.0468` n `18`; unknown avg `-0.0223` n `358`
- 1h: commodity avg `-0.3633` n `12`; crypto_alt avg `0.0296` n `228`; crypto_major avg `-0.2198` n `8`; equity avg `0.1722` n `65`; fx avg `0.0343` n `4`; index avg `-0.0538` n `23`; metal avg `-0.0607` n `18`; unknown avg `0.1043` n `358`
- 4h: commodity avg `-0.9143` n `12`; crypto_alt avg `0.7711` n `228`; crypto_major avg `0.3605` n `8`; equity avg `0.4686` n `65`; fx avg `0.033` n `4`; index avg `0.1529` n `23`; metal avg `1.1811` n `18`; unknown avg `0.3622` n `356`
- 24h: commodity avg `-1.1161` n `7`; crypto_alt avg `0.3981` n `223`; crypto_major avg `-1.4564` n `7`; equity avg `0.6662` n `47`; fx avg `0.1175` n `4`; index avg `0.8371` n `6`; metal avg `1.5701` n `7`; unknown avg `0.8428` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `533`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `533`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.093`, n `533`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0777`, n `529`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `529`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0742`, n `529`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0709`, n `529`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0708`, n `529`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0692`, n `529`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `529`, weak_sample_signal
