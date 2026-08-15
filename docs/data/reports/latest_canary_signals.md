# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T11:22:27.435532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `12`; crypto_alt avg `-0.0346` n `230`; crypto_major avg `0.0042` n `8`; equity avg `0.0115` n `114`; fx avg `-0.0012` n `6`; index avg `0.0005` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0133` n `791`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `-0.1137` n `230`; crypto_major avg `-0.0262` n `8`; equity avg `0.0084` n `114`; fx avg `0.0011` n `6`; index avg `0.0003` n `25`; metal avg `0.0135` n `20`; unknown avg `-0.0785` n `791`
- 4h: commodity avg `0.1123` n `12`; crypto_alt avg `-0.02` n `230`; crypto_major avg `-0.0954` n `8`; equity avg `-0.0001` n `114`; fx avg `-0.0036` n `6`; index avg `-0.0177` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.079` n `791`
- 24h: commodity avg `0.0315` n `12`; crypto_alt avg `1.011` n `230`; crypto_major avg `0.1257` n `8`; equity avg `-0.6655` n `114`; fx avg `0.1189` n `6`; index avg `-0.1568` n `25`; metal avg `0.2039` n `20`; unknown avg `-0.1394` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
