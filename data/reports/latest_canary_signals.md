# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T12:22:31.844207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1361` n `230`; crypto_major avg `-0.0435` n `8`; equity avg `0.0009` n `114`; fx avg `-0.002` n `6`; index avg `0.0149` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0067` n `791`
- 1h: commodity avg `0.0548` n `12`; crypto_alt avg `-0.0792` n `230`; crypto_major avg `-0.0353` n `8`; equity avg `0.0021` n `114`; fx avg `-0.0028` n `6`; index avg `0.0191` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0125` n `791`
- 4h: commodity avg `0.0883` n `12`; crypto_alt avg `-0.0452` n `230`; crypto_major avg `-0.122` n `8`; equity avg `0.0209` n `114`; fx avg `-0.0207` n `6`; index avg `0.016` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0358` n `791`
- 24h: commodity avg `-0.0297` n `12`; crypto_alt avg `1.1583` n `230`; crypto_major avg `0.2241` n `8`; equity avg `-0.4573` n `114`; fx avg `0.1265` n `6`; index avg `-0.1012` n `25`; metal avg `0.0638` n `20`; unknown avg `-0.118` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
