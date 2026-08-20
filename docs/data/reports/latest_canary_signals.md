# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T13:52:30.494042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0375` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `0.533` n `230`; crypto_major avg `0.6843` n `8`; equity avg `-0.6215` n `121`; fx avg `0.018` n `6`; index avg `-0.0998` n `25`; metal avg `-0.0195` n `20`; unknown avg `0.006` n `792`
- 1h: commodity avg `-0.0328` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.2757` n `8`; equity avg `-0.3755` n `121`; fx avg `-0.0056` n `6`; index avg `0.0155` n `25`; metal avg `0.0576` n `20`; unknown avg `0.1412` n `792`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.6563` n `230`; crypto_major avg `0.7046` n `8`; equity avg `-1.3329` n `121`; fx avg `-0.0003` n `6`; index avg `-0.1443` n `25`; metal avg `0.016` n `20`; unknown avg `0.3846` n `792`
- 24h: commodity avg `0.0792` n `12`; crypto_alt avg `7.4889` n `230`; crypto_major avg `12.1591` n `8`; equity avg `0.1977` n `121`; fx avg `0.1736` n `6`; index avg `-0.0273` n `25`; metal avg `0.3121` n `20`; unknown avg `2.7658` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
