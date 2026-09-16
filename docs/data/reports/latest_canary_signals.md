# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T20:37:34.550207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5823` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5415` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.1651` n `234`; crypto_major avg `-0.3656` n `8`; equity avg `-0.0608` n `137`; fx avg `-0.0027` n `6`; index avg `-0.0004` n `27`; metal avg `0.0143` n `20`; unknown avg `3.9391` n `913`
- 1h: commodity avg `0.0325` n `12`; crypto_alt avg `0.7995` n `234`; crypto_major avg `0.5556` n `8`; equity avg `0.6082` n `137`; fx avg `0.0306` n `6`; index avg `0.1086` n `27`; metal avg `0.0641` n `20`; unknown avg `3.2945` n `869`
- 4h: commodity avg `-0.0924` n `12`; crypto_alt avg `1.25` n `234`; crypto_major avg `0.9947` n `8`; equity avg `-0.5876` n `137`; fx avg `0.0647` n `6`; index avg `-0.2011` n `27`; metal avg `-0.5468` n `20`; unknown avg `6.9663` n `829`
- 24h: commodity avg `-0.6086` n `12`; crypto_alt avg `-0.0688` n `234`; crypto_major avg `0.883` n `8`; equity avg `0.6945` n `137`; fx avg `0.0957` n `6`; index avg `0.0129` n `27`; metal avg `-0.2631` n `20`; unknown avg `2.1621` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
