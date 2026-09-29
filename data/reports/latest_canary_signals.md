# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T12:52:33.497722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1204` n `12`; crypto_alt avg `-0.1765` n `234`; crypto_major avg `-0.1177` n `8`; equity avg `0.0189` n `141`; fx avg `-0.0095` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0397` n `20`; unknown avg `0.1368` n `963`
- 1h: commodity avg `-0.1549` n `12`; crypto_alt avg `-0.3025` n `234`; crypto_major avg `0.297` n `8`; equity avg `-0.0027` n `141`; fx avg `-0.024` n `6`; index avg `-0.0263` n `26`; metal avg `-0.1445` n `20`; unknown avg `-0.4857` n `955`
- 4h: commodity avg `-0.4166` n `12`; crypto_alt avg `1.0413` n `234`; crypto_major avg `1.0945` n `8`; equity avg `0.3073` n `141`; fx avg `-0.0514` n `6`; index avg `0.0439` n `26`; metal avg `0.047` n `20`; unknown avg `199.5836` n `955`
- 24h: commodity avg `-0.6888` n `12`; crypto_alt avg `0.6639` n `234`; crypto_major avg `0.5788` n `8`; equity avg `-0.2491` n `141`; fx avg `-0.1275` n `6`; index avg `-0.075` n `26`; metal avg `-0.1648` n `20`; unknown avg `71.8128` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
