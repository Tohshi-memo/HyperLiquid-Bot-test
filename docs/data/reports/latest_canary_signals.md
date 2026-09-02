# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T19:52:27.322418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1219` n `232`; crypto_major avg `0.1286` n `8`; equity avg `0.043` n `133`; fx avg `-0.0022` n `6`; index avg `0.0011` n `26`; metal avg `0.0303` n `20`; unknown avg `0.6653` n `792`
- 1h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.2124` n `232`; crypto_major avg `-0.1033` n `8`; equity avg `0.2043` n `133`; fx avg `-0.0031` n `6`; index avg `0.0221` n `26`; metal avg `0.0616` n `20`; unknown avg `0.0385` n `790`
- 4h: commodity avg `0.0658` n `12`; crypto_alt avg `-0.0102` n `232`; crypto_major avg `0.0675` n `8`; equity avg `0.8375` n `133`; fx avg `-0.0083` n `6`; index avg `0.0532` n `26`; metal avg `0.1083` n `20`; unknown avg `-0.8309` n `790`
- 24h: commodity avg `0.193` n `12`; crypto_alt avg `-0.528` n `232`; crypto_major avg `-0.4534` n `8`; equity avg `0.8428` n `133`; fx avg `-0.3597` n `6`; index avg `0.1486` n `26`; metal avg `0.5226` n `20`; unknown avg `-0.1361` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
