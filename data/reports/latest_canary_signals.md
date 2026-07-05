# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T12:22:27.668639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.1563` n `229`; crypto_major avg `0.2317` n `8`; equity avg `0.0304` n `88`; fx avg `-0.0022` n `6`; index avg `0.004` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0902` n `765`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0439` n `229`; crypto_major avg `0.2321` n `8`; equity avg `0.0243` n `88`; fx avg `0.0003` n `6`; index avg `0.0225` n `25`; metal avg `0.0134` n `20`; unknown avg `0.0637` n `765`
- 4h: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.3932` n `229`; crypto_major avg `0.009` n `8`; equity avg `0.037` n `88`; fx avg `0.0007` n `6`; index avg `0.0156` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.0401` n `765`
- 24h: commodity avg `-0.0455` n `12`; crypto_alt avg `-1.3333` n `229`; crypto_major avg `-0.5559` n `8`; equity avg `0.3199` n `88`; fx avg `0.0101` n `6`; index avg `0.0608` n `25`; metal avg `0.0868` n `20`; unknown avg `-1.1783` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
