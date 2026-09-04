# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T00:07:31.843300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.1348` n `232`; crypto_major avg `-0.2074` n `8`; equity avg `0.137` n `133`; fx avg `-0.0333` n `6`; index avg `-0.0005` n `26`; metal avg `0.0127` n `20`; unknown avg `0.0792` n `790`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0974` n `232`; crypto_major avg `0.0559` n `8`; equity avg `0.1778` n `133`; fx avg `-0.0599` n `6`; index avg `-0.007` n `26`; metal avg `0.0215` n `20`; unknown avg `-0.1214` n `790`
- 4h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.3955` n `232`; crypto_major avg `-0.5202` n `8`; equity avg `0.0701` n `133`; fx avg `-0.0357` n `6`; index avg `-0.0082` n `26`; metal avg `0.0107` n `20`; unknown avg `1.0193` n `766`
- 24h: commodity avg `-0.0916` n `12`; crypto_alt avg `3.7689` n `232`; crypto_major avg `4.9335` n `8`; equity avg `1.3572` n `133`; fx avg `-0.3343` n `6`; index avg `0.201` n `26`; metal avg `0.826` n `20`; unknown avg `1.1064` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
