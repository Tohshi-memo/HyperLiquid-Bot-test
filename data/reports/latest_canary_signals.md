# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T13:52:24.253264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.037` n `13`; crypto_alt avg `0.1619` n `239`; crypto_major avg `0.2159` n `8`; equity avg `-0.0767` n `161`; fx avg `0.0206` n `6`; index avg `-0.0033` n `27`; metal avg `-0.0191` n `20`; unknown avg `0.4135` n `1261`
- 1h: commodity avg `-0.0652` n `13`; crypto_alt avg `0.1545` n `239`; crypto_major avg `0.0085` n `8`; equity avg `-0.1112` n `161`; fx avg `-0.0289` n `6`; index avg `-0.0149` n `27`; metal avg `-0.0514` n `20`; unknown avg `19.1255` n `1255`
- 4h: commodity avg `0.1426` n `13`; crypto_alt avg `0.7902` n `239`; crypto_major avg `0.4334` n `8`; equity avg `0.4266` n `161`; fx avg `0.0516` n `6`; index avg `0.026` n `27`; metal avg `-0.0934` n `20`; unknown avg `19.4045` n `1247`
- 24h: commodity avg `1.1109` n `13`; crypto_alt avg `-0.0452` n `239`; crypto_major avg `-0.538` n `8`; equity avg `4.4593` n `161`; fx avg `-0.199` n `6`; index avg `0.3829` n `27`; metal avg `0.287` n `20`; unknown avg `2.3218` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2992`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
