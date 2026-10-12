# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T12:22:28.149494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `13`; crypto_alt avg `0.0202` n `235`; crypto_major avg `-0.0849` n `8`; equity avg `0.1231` n `151`; fx avg `-0.0118` n `6`; index avg `0.0229` n `26`; metal avg `-0.0362` n `20`; unknown avg `-0.08` n `1134`
- 1h: commodity avg `0.0174` n `13`; crypto_alt avg `-0.065` n `235`; crypto_major avg `-0.2467` n `8`; equity avg `0.0047` n `151`; fx avg `0.0028` n `6`; index avg `0.0149` n `26`; metal avg `-0.0324` n `20`; unknown avg `0.0322` n `1125`
- 4h: commodity avg `0.3063` n `13`; crypto_alt avg `-0.8527` n `235`; crypto_major avg `-0.6675` n `8`; equity avg `-0.4326` n `151`; fx avg `-0.0135` n `6`; index avg `-0.0831` n `26`; metal avg `-0.014` n `20`; unknown avg `-0.0588` n `1019`
- 24h: commodity avg `0.0741` n `13`; crypto_alt avg `1.2825` n `235`; crypto_major avg `0.5784` n `8`; equity avg `-1.344` n `151`; fx avg `-0.1335` n `6`; index avg `-0.1454` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.5722` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2458`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
