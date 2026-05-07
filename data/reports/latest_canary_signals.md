# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T18:37:15.366435+00:00`
- Correlation status: `ready`
- Asset price records: `574`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7711` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5983` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1364` n `12`; crypto_alt avg `0.2612` n `228`; crypto_major avg `0.0198` n `8`; equity avg `-0.0241` n `65`; fx avg `0.0191` n `5`; index avg `-0.1453` n `23`; metal avg `-0.0359` n `18`; unknown avg `0.0087` n `365`
- 1h: commodity avg `-0.3796` n `12`; crypto_alt avg `1.0593` n `228`; crypto_major avg `0.4301` n `8`; equity avg `0.0011` n `65`; fx avg `-0.0021` n `5`; index avg `-0.0889` n `23`; metal avg `0.0602` n `18`; unknown avg `0.1278` n `365`
- 4h: commodity avg `1.6941` n `12`; crypto_alt avg `1.5665` n `228`; crypto_major avg `0.2521` n `8`; equity avg `-1.519` n `65`; fx avg `0.0625` n `5`; index avg `-0.8396` n `23`; metal avg `-1.3462` n `18`; unknown avg `-0.0283` n `365`
- 24h: commodity avg `0.4596` n `12`; crypto_alt avg `1.7509` n `228`; crypto_major avg `-1.4367` n `8`; equity avg `-1.1292` n `65`; fx avg `0.1911` n `5`; index avg `-0.7781` n `23`; metal avg `0.5004` n `18`; unknown avg `0.1175` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `570`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `570`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `570`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `570`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0926`, n `566`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `566`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `566`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0882`, n `566`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.088`, n `566`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0753`, n `566`, weak_sample_signal
