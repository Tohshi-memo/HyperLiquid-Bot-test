# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T18:07:43.417239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1447` n `12`; crypto_alt avg `-0.0694` n `231`; crypto_major avg `-0.1605` n `8`; equity avg `-0.1922` n `127`; fx avg `0.0027` n `6`; index avg `-0.0333` n `26`; metal avg `-0.0282` n `20`; unknown avg `-0.0052` n `792`
- 1h: commodity avg `0.2929` n `12`; crypto_alt avg `-0.2118` n `231`; crypto_major avg `-0.1877` n `8`; equity avg `-0.1511` n `127`; fx avg `0.01` n `6`; index avg `-0.0721` n `26`; metal avg `0.0134` n `20`; unknown avg `0.133` n `792`
- 4h: commodity avg `0.1847` n `12`; crypto_alt avg `0.7022` n `231`; crypto_major avg `1.2528` n `8`; equity avg `0.0882` n `127`; fx avg `-0.0187` n `6`; index avg `0.0423` n `26`; metal avg `0.3347` n `20`; unknown avg `0.1716` n `792`
- 24h: commodity avg `0.5407` n `12`; crypto_alt avg `3.6209` n `231`; crypto_major avg `4.161` n `8`; equity avg `1.4389` n `127`; fx avg `-0.0495` n `6`; index avg `0.1391` n `26`; metal avg `0.1669` n `20`; unknown avg `0.961` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
