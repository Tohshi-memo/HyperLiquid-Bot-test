# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T21:07:37.552184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.2177` n `232`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0324` n `133`; fx avg `-0.007` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0198` n `20`; unknown avg `0.0156` n `784`
- 1h: commodity avg `0.0606` n `12`; crypto_alt avg `-0.1922` n `232`; crypto_major avg `-0.0097` n `8`; equity avg `-0.1712` n `133`; fx avg `-0.0139` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0181` n `20`; unknown avg `0.0576` n `776`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.3176` n `232`; crypto_major avg `0.6153` n `8`; equity avg `0.5835` n `133`; fx avg `-0.0319` n `6`; index avg `0.003` n `26`; metal avg `0.0999` n `20`; unknown avg `-0.144` n `772`
- 24h: commodity avg `0.1654` n `12`; crypto_alt avg `-0.1618` n `232`; crypto_major avg `-0.0826` n `8`; equity avg `0.609` n `133`; fx avg `-0.3845` n `6`; index avg `0.0759` n `26`; metal avg `0.4653` n `20`; unknown avg `18675.1719` n `755`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
