# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T13:52:25.339662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `13`; crypto_alt avg `-0.09` n `239`; crypto_major avg `-0.0603` n `8`; equity avg `-0.0935` n `162`; fx avg `0.0102` n `6`; index avg `-0.0049` n `27`; metal avg `0.0111` n `20`; unknown avg `7.9028` n `1264`
- 1h: commodity avg `0.0627` n `13`; crypto_alt avg `-0.2799` n `239`; crypto_major avg `-0.098` n `8`; equity avg `-0.3945` n `162`; fx avg `-0.0214` n `6`; index avg `-0.0486` n `27`; metal avg `-0.155` n `20`; unknown avg `8.9054` n `1224`
- 4h: commodity avg `0.1649` n `13`; crypto_alt avg `0.9929` n `239`; crypto_major avg `0.935` n `8`; equity avg `1.1982` n `162`; fx avg `-0.0157` n `6`; index avg `0.0813` n `27`; metal avg `-0.0834` n `20`; unknown avg `3.996` n `1218`
- 24h: commodity avg `-0.3503` n `13`; crypto_alt avg `1.779` n `239`; crypto_major avg `2.0774` n `8`; equity avg `-1.1155` n `162`; fx avg `-0.0594` n `6`; index avg `-0.1489` n `27`; metal avg `-0.2141` n `20`; unknown avg `7.0098` n `1107`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
