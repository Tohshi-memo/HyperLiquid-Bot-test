# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T22:07:27.963818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `13`; crypto_alt avg `-0.1699` n `235`; crypto_major avg `-0.0461` n `8`; equity avg `-0.0084` n `150`; fx avg `0.0001` n `6`; index avg `-0.004` n `26`; metal avg `-0.0086` n `20`; unknown avg `-0.0729` n `1114`
- 1h: commodity avg `-0.1716` n `13`; crypto_alt avg `0.111` n `235`; crypto_major avg `-0.0274` n `8`; equity avg `-0.047` n `150`; fx avg `0.0024` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0202` n `20`; unknown avg `-0.1044` n `1106`
- 4h: commodity avg `-0.2573` n `13`; crypto_alt avg `-0.1099` n `235`; crypto_major avg `-0.2848` n `8`; equity avg `-0.032` n `150`; fx avg `-0.0001` n `6`; index avg `0.0141` n `26`; metal avg `-0.0282` n `20`; unknown avg `0.2286` n `1026`
- 24h: commodity avg `-0.2037` n `13`; crypto_alt avg `1.655` n `235`; crypto_major avg `0.2427` n `8`; equity avg `0.7975` n `150`; fx avg `0.0194` n `6`; index avg `0.1479` n `26`; metal avg `0.5922` n `20`; unknown avg `12.7314` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
