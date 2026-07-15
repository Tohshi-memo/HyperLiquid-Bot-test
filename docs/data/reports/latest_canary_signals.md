# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T02:22:27.017232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.075` n `230`; crypto_major avg `-0.0454` n `8`; equity avg `0.0531` n `93`; fx avg `-0.0018` n `6`; index avg `0.0059` n `25`; metal avg `-0.0718` n `20`; unknown avg `-0.0094` n `767`
- 1h: commodity avg `0.0822` n `12`; crypto_alt avg `-0.2061` n `230`; crypto_major avg `-0.2502` n `8`; equity avg `0.497` n `93`; fx avg `0.0232` n `6`; index avg `0.0758` n `25`; metal avg `-0.1575` n `20`; unknown avg `-0.2016` n `767`
- 4h: commodity avg `0.0549` n `12`; crypto_alt avg `-0.0628` n `230`; crypto_major avg `-0.4907` n `8`; equity avg `0.991` n `93`; fx avg `0.0342` n `6`; index avg `0.1682` n `25`; metal avg `-0.0596` n `20`; unknown avg `-0.342` n `765`
- 24h: commodity avg `0.2401` n `12`; crypto_alt avg `1.8644` n `230`; crypto_major avg `2.8628` n `8`; equity avg `2.592` n `92`; fx avg `0.0576` n `6`; index avg `0.7337` n `25`; metal avg `0.4222` n `20`; unknown avg `0.2008` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
