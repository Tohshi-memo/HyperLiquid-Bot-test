# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T23:07:33.087659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.2371` n `232`; crypto_major avg `0.1954` n `8`; equity avg `0.0582` n `133`; fx avg `0.0025` n `6`; index avg `0.011` n `26`; metal avg `0.0162` n `20`; unknown avg `0.0661` n `790`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `0.1668` n `232`; crypto_major avg `0.1216` n `8`; equity avg `0.072` n `133`; fx avg `0.0205` n `6`; index avg `0.0303` n `26`; metal avg `-0.0056` n `20`; unknown avg `16.5947` n `790`
- 4h: commodity avg `0.0344` n `12`; crypto_alt avg `0.0599` n `232`; crypto_major avg `-0.0327` n `8`; equity avg `0.1762` n `133`; fx avg `-0.0194` n `6`; index avg `0.025` n `26`; metal avg `0.0318` n `20`; unknown avg `-0.3093` n `772`
- 24h: commodity avg `0.1452` n `12`; crypto_alt avg `-0.0025` n `232`; crypto_major avg `-0.2276` n `8`; equity avg `1.1077` n `133`; fx avg `-0.385` n `6`; index avg `0.1441` n `26`; metal avg `0.4612` n `20`; unknown avg `-0.5211` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
