# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T16:07:38.199045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0879` n `232`; crypto_major avg `-0.114` n `8`; equity avg `-0.194` n `128`; fx avg `-0.0156` n `6`; index avg `-0.0391` n `26`; metal avg `0.0143` n `20`; unknown avg `0.0173` n `792`
- 1h: commodity avg `0.039` n `12`; crypto_alt avg `-0.1272` n `232`; crypto_major avg `0.0922` n `8`; equity avg `-0.0965` n `128`; fx avg `-0.0086` n `6`; index avg `-0.0605` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.0002` n `792`
- 4h: commodity avg `-0.0531` n `12`; crypto_alt avg `-0.4299` n `232`; crypto_major avg `0.0543` n `8`; equity avg `-0.2288` n `128`; fx avg `0.0445` n `6`; index avg `-0.15` n `26`; metal avg `-0.3564` n `20`; unknown avg `0.8701` n `790`
- 24h: commodity avg `0.5522` n `12`; crypto_alt avg `-1.2107` n `231`; crypto_major avg `-1.4999` n `8`; equity avg `-0.6605` n `128`; fx avg `-0.093` n `6`; index avg `-0.2399` n `26`; metal avg `-0.5463` n `20`; unknown avg `0.154` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
