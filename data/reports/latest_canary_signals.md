# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T13:22:28.878036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.0406` n `230`; crypto_major avg `0.0239` n `8`; equity avg `0.007` n `114`; fx avg `-0.0076` n `6`; index avg `0.0002` n `25`; metal avg `-0.001` n `20`; unknown avg `0.0276` n `791`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.0516` n `230`; crypto_major avg `0.0795` n `8`; equity avg `-0.0799` n `114`; fx avg `-0.0074` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.1093` n `791`
- 4h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.0727` n `230`; crypto_major avg `-0.0532` n `8`; equity avg `-0.1201` n `114`; fx avg `-0.0184` n `6`; index avg `-0.0093` n `25`; metal avg `0.0045` n `20`; unknown avg `0.1387` n `791`
- 24h: commodity avg `0.0536` n `12`; crypto_alt avg `0.0888` n `230`; crypto_major avg `0.071` n `8`; equity avg `0.237` n `114`; fx avg `-0.017` n `6`; index avg `0.033` n `25`; metal avg `0.0364` n `20`; unknown avg `0.1831` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
