# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T14:22:37.229782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1181` n `13`; crypto_alt avg `-0.1542` n `235`; crypto_major avg `-0.243` n `8`; equity avg `0.216` n `144`; fx avg `-0.0261` n `6`; index avg `0.0717` n `26`; metal avg `0.025` n `20`; unknown avg `-0.0103` n `1057`
- 1h: commodity avg `-0.047` n `13`; crypto_alt avg `-0.0638` n `235`; crypto_major avg `0.1721` n `8`; equity avg `0.0896` n `144`; fx avg `-0.081` n `6`; index avg `0.103` n `26`; metal avg `-0.0697` n `20`; unknown avg `3.1684` n `1039`
- 4h: commodity avg `-0.2994` n `13`; crypto_alt avg `-0.1916` n `235`; crypto_major avg `0.0544` n `8`; equity avg `0.1278` n `144`; fx avg `-0.0808` n `6`; index avg `0.1478` n `26`; metal avg `-0.0277` n `20`; unknown avg `3.6842` n `1033`
- 24h: commodity avg `-0.4118` n `13`; crypto_alt avg `0.8472` n `235`; crypto_major avg `1.2002` n `8`; equity avg `0.2064` n `144`; fx avg `-0.1392` n `6`; index avg `0.0614` n `26`; metal avg `0.2003` n `20`; unknown avg `-0.4314` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
