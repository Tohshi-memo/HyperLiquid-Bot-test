# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T23:22:32.037673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0077` n `232`; crypto_major avg `0.0861` n `8`; equity avg `-0.0104` n `133`; fx avg `-0.0028` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0107` n `20`; unknown avg `2.8824` n `792`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `-0.4143` n `232`; crypto_major avg `-0.0833` n `8`; equity avg `0.018` n `133`; fx avg `0.013` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0288` n `20`; unknown avg `3.2111` n `790`
- 4h: commodity avg `0.0755` n `12`; crypto_alt avg `-0.7678` n `232`; crypto_major avg `-0.3798` n `8`; equity avg `-0.0635` n `133`; fx avg `0.0237` n `6`; index avg `-0.008` n `26`; metal avg `-0.0296` n `20`; unknown avg `212.1883` n `766`
- 24h: commodity avg `-0.0744` n `12`; crypto_alt avg `3.9032` n `232`; crypto_major avg `5.2918` n `8`; equity avg `1.2409` n `133`; fx avg `-0.2138` n `6`; index avg `0.1638` n `26`; metal avg `0.8074` n `20`; unknown avg `3.5636` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
