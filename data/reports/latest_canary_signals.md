# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T17:37:35.428035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `13`; crypto_alt avg `0.3595` n `235`; crypto_major avg `0.1464` n `8`; equity avg `0.2314` n `150`; fx avg `0.0147` n `6`; index avg `0.0322` n `26`; metal avg `0.0333` n `20`; unknown avg `0.2922` n `1076`
- 1h: commodity avg `0.0827` n `13`; crypto_alt avg `0.1586` n `235`; crypto_major avg `0.01` n `8`; equity avg `0.0716` n `150`; fx avg `0.0122` n `6`; index avg `-0.0094` n `26`; metal avg `0.028` n `20`; unknown avg `-0.2266` n `1074`
- 4h: commodity avg `0.4365` n `13`; crypto_alt avg `-0.3411` n `235`; crypto_major avg `-0.7249` n `8`; equity avg `0.0781` n `150`; fx avg `0.0249` n `6`; index avg `-0.0222` n `26`; metal avg `0.0556` n `20`; unknown avg `5.8301` n `1018`
- 24h: commodity avg `0.0041` n `13`; crypto_alt avg `0.3155` n `235`; crypto_major avg `-0.0955` n `8`; equity avg `0.7598` n `149`; fx avg `0.1147` n `6`; index avg `0.0662` n `26`; metal avg `0.1051` n `20`; unknown avg `381.9095` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
