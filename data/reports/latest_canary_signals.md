# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T12:56:02.471755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `0.0508` n `230`; crypto_major avg `0.0222` n `8`; equity avg `0.0058` n `114`; fx avg `0.0027` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0011` n `791`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0968` n `230`; crypto_major avg `0.0079` n `8`; equity avg `-0.0012` n `114`; fx avg `0.0027` n `6`; index avg `0.0169` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.0128` n `791`
- 4h: commodity avg `0.0637` n `12`; crypto_alt avg `-0.1021` n `230`; crypto_major avg `0.0213` n `8`; equity avg `0.0126` n `114`; fx avg `-0.0041` n `6`; index avg `0.0104` n `25`; metal avg `0.003` n `20`; unknown avg `-0.0448` n `791`
- 24h: commodity avg `0.0523` n `12`; crypto_alt avg `1.12` n `230`; crypto_major avg `0.3334` n `8`; equity avg `-0.6491` n `114`; fx avg `0.1409` n `6`; index avg `-0.1341` n `25`; metal avg `0.1067` n `20`; unknown avg `-0.0637` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
