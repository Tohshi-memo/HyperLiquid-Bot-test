# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T01:52:18.412403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0742` n `12`; crypto_alt avg `0.1445` n `228`; crypto_major avg `0.0761` n `8`; equity avg `-0.0285` n `69`; fx avg `-0.0089` n `6`; index avg `0.0253` n `23`; metal avg `-0.131` n `18`; unknown avg `-0.0123` n `417`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.3028` n `228`; crypto_major avg `-0.4012` n `8`; equity avg `-0.2065` n `69`; fx avg `-0.0001` n `6`; index avg `-0.0575` n `23`; metal avg `0.2012` n `18`; unknown avg `-0.1059` n `417`
- 4h: commodity avg `-0.0522` n `12`; crypto_alt avg `-0.2038` n `228`; crypto_major avg `-0.5527` n `8`; equity avg `0.1359` n `69`; fx avg `0.0819` n `6`; index avg `-0.0323` n `23`; metal avg `0.2056` n `18`; unknown avg `-0.3316` n `417`
- 24h: commodity avg `0.5065` n `12`; crypto_alt avg `-1.0288` n `228`; crypto_major avg `0.3537` n `8`; equity avg `2.5409` n `69`; fx avg `0.0422` n `6`; index avg `0.8145` n `23`; metal avg `1.6566` n `18`; unknown avg `0.2547` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
