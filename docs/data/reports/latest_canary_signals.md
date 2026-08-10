# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T22:07:29.154696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.1205` n `230`; crypto_major avg `-0.1544` n `8`; equity avg `0.0316` n `113`; fx avg `0.0089` n `6`; index avg `0.007` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.0629` n `785`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.479` n `230`; crypto_major avg `-0.3711` n `8`; equity avg `-0.0614` n `113`; fx avg `0.0067` n `6`; index avg `0.0093` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.0749` n `785`
- 4h: commodity avg `0.025` n `12`; crypto_alt avg `-0.6293` n `230`; crypto_major avg `-0.0857` n `8`; equity avg `-0.407` n `113`; fx avg `0.0148` n `6`; index avg `-0.0026` n `25`; metal avg `0.2092` n `20`; unknown avg `0.9507` n `785`
- 24h: commodity avg `0.7987` n `12`; crypto_alt avg `-1.8072` n `230`; crypto_major avg `-1.6384` n `8`; equity avg `-1.6898` n `113`; fx avg `0.2637` n `6`; index avg `-0.0361` n `25`; metal avg `0.3226` n `20`; unknown avg `103.6189` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
