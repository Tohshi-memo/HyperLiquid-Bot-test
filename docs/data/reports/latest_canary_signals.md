# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T14:07:32.887136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0508` n `13`; crypto_alt avg `-0.1411` n `236`; crypto_major avg `0.0334` n `8`; equity avg `0.0015` n `151`; fx avg `0.0152` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0744` n `20`; unknown avg `0.2373` n `1086`
- 1h: commodity avg `-0.1326` n `13`; crypto_alt avg `-0.2052` n `236`; crypto_major avg `-0.1621` n `8`; equity avg `-1.1021` n `151`; fx avg `0.0453` n `6`; index avg `-0.1668` n `26`; metal avg `0.0385` n `20`; unknown avg `42.1849` n `1078`
- 4h: commodity avg `-0.2631` n `13`; crypto_alt avg `-0.2602` n `236`; crypto_major avg `-0.203` n `8`; equity avg `-1.5783` n `151`; fx avg `0.06` n `6`; index avg `-0.1634` n `26`; metal avg `-0.0203` n `20`; unknown avg `2.2139` n `1072`
- 24h: commodity avg `-0.336` n `13`; crypto_alt avg `3.9956` n `236`; crypto_major avg `2.3943` n `8`; equity avg `1.3382` n `151`; fx avg `0.0143` n `6`; index avg `0.0783` n `26`; metal avg `0.266` n `20`; unknown avg `0.1006` n `930`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0827`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `666`, weak_sample_signal
