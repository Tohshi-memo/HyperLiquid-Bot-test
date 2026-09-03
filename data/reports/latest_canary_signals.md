# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T00:52:24.337735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.0865` n `232`; crypto_major avg `0.0148` n `8`; equity avg `0.016` n `133`; fx avg `-0.0403` n `6`; index avg `-0.01` n `26`; metal avg `0.0416` n `20`; unknown avg `-0.1694` n `792`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.0492` n `232`; crypto_major avg `-0.2801` n `8`; equity avg `-0.0629` n `133`; fx avg `-0.0269` n `6`; index avg `-0.0681` n `26`; metal avg `0.0159` n `20`; unknown avg `0.0044` n `790`
- 4h: commodity avg `0.0811` n `12`; crypto_alt avg `-0.0263` n `232`; crypto_major avg `-0.2568` n `8`; equity avg `0.2014` n `133`; fx avg `-0.0075` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0108` n `20`; unknown avg `-0.0905` n `784`
- 24h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1458` n `232`; crypto_major avg `-0.225` n `8`; equity avg `1.0517` n `133`; fx avg `-0.3379` n `6`; index avg `0.0642` n `26`; metal avg `0.5625` n `20`; unknown avg `-0.5364` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
