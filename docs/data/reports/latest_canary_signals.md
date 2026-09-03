# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T14:07:27.370938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `-0.0923` n `232`; crypto_major avg `-0.0485` n `8`; equity avg `-0.4132` n `133`; fx avg `0.009` n `6`; index avg `-0.0928` n `26`; metal avg `0.0605` n `20`; unknown avg `0.2255` n `790`
- 1h: commodity avg `0.0227` n `12`; crypto_alt avg `-0.2492` n `232`; crypto_major avg `0.1794` n `8`; equity avg `-0.4764` n `133`; fx avg `0.0002` n `6`; index avg `-0.0439` n `26`; metal avg `-0.085` n `20`; unknown avg `0.6452` n `790`
- 4h: commodity avg `-0.052` n `12`; crypto_alt avg `0.2143` n `232`; crypto_major avg `1.1641` n `8`; equity avg `0.0139` n `133`; fx avg `-0.0602` n `6`; index avg `0.0722` n `26`; metal avg `0.2727` n `20`; unknown avg `4.1788` n `790`
- 24h: commodity avg `0.58` n `12`; crypto_alt avg `1.5773` n `232`; crypto_major avg `1.9826` n `8`; equity avg `0.6319` n `133`; fx avg `-0.3128` n `6`; index avg `0.019` n `26`; metal avg `0.4033` n `20`; unknown avg `0.1099` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
