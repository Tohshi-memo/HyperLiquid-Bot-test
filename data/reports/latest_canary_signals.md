# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T23:37:27.979869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0491` n `230`; crypto_major avg `0.0117` n `8`; equity avg `0.0061` n `114`; fx avg `0.001` n `6`; index avg `0.0003` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0102` n `791`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.386` n `230`; crypto_major avg `-0.1756` n `8`; equity avg `0.0026` n `114`; fx avg `-0.0` n `6`; index avg `0.0164` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.1937` n `791`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.4583` n `230`; crypto_major avg `-0.2111` n `8`; equity avg `-0.0002` n `114`; fx avg `0.0003` n `6`; index avg `0.0035` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.1306` n `791`
- 24h: commodity avg `-0.0939` n `12`; crypto_alt avg `0.1653` n `230`; crypto_major avg `0.0717` n `8`; equity avg `0.1527` n `114`; fx avg `0.0851` n `6`; index avg `0.0067` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.1304` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
