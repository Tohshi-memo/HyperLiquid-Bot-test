# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:22:28.596082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `0.0087` n `230`; crypto_major avg `0.0524` n `8`; equity avg `0.0184` n `114`; fx avg `0.0005` n `6`; index avg `0.0054` n `25`; metal avg `-0.0061` n `20`; unknown avg `0.1173` n `791`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.08` n `230`; crypto_major avg `0.1369` n `8`; equity avg `0.0221` n `114`; fx avg `0.0941` n `6`; index avg `0.0113` n `25`; metal avg `-0.0161` n `20`; unknown avg `0.1351` n `791`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.2866` n `230`; crypto_major avg `0.533` n `8`; equity avg `0.0117` n `114`; fx avg `0.0638` n `6`; index avg `0.0057` n `25`; metal avg `0.0134` n `20`; unknown avg `0.5448` n `791`
- 24h: commodity avg `0.1664` n `12`; crypto_alt avg `0.3224` n `230`; crypto_major avg `-0.2759` n `8`; equity avg `-0.1642` n `114`; fx avg `0.2132` n `6`; index avg `-0.0376` n `25`; metal avg `0.3857` n `20`; unknown avg `0.0865` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
