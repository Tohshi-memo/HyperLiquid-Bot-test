# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T16:37:27.358700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.28` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.4025` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.1606` n `233`; crypto_major avg `0.1671` n `8`; equity avg `0.009` n `136`; fx avg `0.0001` n `6`; index avg `-0.0057` n `26`; metal avg `0.0327` n `20`; unknown avg `0.1368` n `790`
- 1h: commodity avg `0.0472` n `12`; crypto_alt avg `-1.3019` n `233`; crypto_major avg `-1.4382` n `8`; equity avg `-0.2806` n `136`; fx avg `0.0051` n `6`; index avg `-0.0357` n `26`; metal avg `-0.0771` n `20`; unknown avg `1.6239` n `788`
- 4h: commodity avg `0.1986` n `12`; crypto_alt avg `0.8262` n `233`; crypto_major avg `0.9253` n `8`; equity avg `0.0312` n `136`; fx avg `-0.0267` n `6`; index avg `0.0627` n `26`; metal avg `0.0687` n `20`; unknown avg `-0.0556` n `772`
- 24h: commodity avg `-0.3367` n `12`; crypto_alt avg `2.0609` n `233`; crypto_major avg `2.4591` n `8`; equity avg `0.574` n `136`; fx avg `-0.1595` n `6`; index avg `0.3027` n `26`; metal avg `0.0838` n `20`; unknown avg `2.2598` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
