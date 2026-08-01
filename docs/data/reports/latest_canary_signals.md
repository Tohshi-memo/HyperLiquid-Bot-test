# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T17:22:27.388465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.1474` n `230`; crypto_major avg `-0.2339` n `8`; equity avg `-0.0304` n `102`; fx avg `0.0007` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0062` n `782`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.2923` n `230`; crypto_major avg `-0.2455` n `8`; equity avg `-0.0359` n `102`; fx avg `-0.0008` n `6`; index avg `0.0063` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0307` n `782`
- 4h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.19` n `230`; crypto_major avg `-0.2386` n `8`; equity avg `-0.1224` n `102`; fx avg `-0.0003` n `6`; index avg `-0.003` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.137` n `782`
- 24h: commodity avg `0.6316` n `12`; crypto_alt avg `-0.1176` n `230`; crypto_major avg `-0.6449` n `8`; equity avg `-0.8798` n `102`; fx avg `-0.1206` n `6`; index avg `-0.1055` n `25`; metal avg `0.0193` n `20`; unknown avg `4.2991` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
