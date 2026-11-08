# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T15:07:47.320400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.0802` n `239`; crypto_major avg `-0.1082` n `8`; equity avg `-0.0384` n `158`; fx avg `-0.0001` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0114` n `20`; unknown avg `3.8628` n `1256`
- 1h: commodity avg `-0.0006` n `13`; crypto_alt avg `0.1341` n `239`; crypto_major avg `0.1689` n `8`; equity avg `-0.019` n `158`; fx avg `0.0051` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0103` n `20`; unknown avg `0.3963` n `1248`
- 4h: commodity avg `0.0593` n `13`; crypto_alt avg `-0.3193` n `239`; crypto_major avg `0.2485` n `8`; equity avg `0.0329` n `158`; fx avg `-0.0092` n `6`; index avg `-0.016` n `27`; metal avg `-0.0089` n `20`; unknown avg `0.4159` n `1242`
- 24h: commodity avg `0.1004` n `13`; crypto_alt avg `-1.3766` n `239`; crypto_major avg `-0.1109` n `8`; equity avg `0.1725` n `158`; fx avg `0.0242` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0498` n `20`; unknown avg `7.7014` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
