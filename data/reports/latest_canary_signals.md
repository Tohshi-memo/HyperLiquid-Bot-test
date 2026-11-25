# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T10:22:30.776243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0288` n `239`; crypto_major avg `-0.0875` n `8`; equity avg `-0.0843` n `168`; fx avg `-0.0014` n `6`; index avg `-0.0278` n `27`; metal avg `-0.0845` n `20`; unknown avg `31.6237` n `1263`
- 1h: commodity avg `0.1825` n `13`; crypto_alt avg `-0.3819` n `239`; crypto_major avg `-0.1064` n `8`; equity avg `-0.3257` n `168`; fx avg `-0.0072` n `6`; index avg `-0.059` n `27`; metal avg `-0.0148` n `20`; unknown avg `242.094` n `1259`
- 4h: commodity avg `0.1025` n `13`; crypto_alt avg `-0.8434` n `239`; crypto_major avg `-0.8922` n `8`; equity avg `-1.4996` n `168`; fx avg `-0.0249` n `6`; index avg `-0.186` n `27`; metal avg `-0.0275` n `20`; unknown avg `0.1996` n `1233`
- 24h: commodity avg `0.3801` n `13`; crypto_alt avg `-2.2259` n `239`; crypto_major avg `-2.9018` n `8`; equity avg `-5.0471` n `167`; fx avg `0.0075` n `6`; index avg `-0.4726` n `27`; metal avg `-0.8473` n `20`; unknown avg `486.3695` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
