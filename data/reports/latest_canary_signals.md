# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T14:22:19.201351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.0669` n `228`; crypto_major avg `-0.0653` n `8`; equity avg `0.0227` n `69`; fx avg `0.0025` n `6`; index avg `0.0106` n `23`; metal avg `0.0051` n `18`; unknown avg `-0.0545` n `421`
- 1h: commodity avg `0.0553` n `12`; crypto_alt avg `0.0029` n `228`; crypto_major avg `0.0971` n `8`; equity avg `0.0751` n `69`; fx avg `0.0183` n `6`; index avg `0.0946` n `23`; metal avg `0.0043` n `18`; unknown avg `0.071` n `421`
- 4h: commodity avg `0.2738` n `12`; crypto_alt avg `0.0976` n `228`; crypto_major avg `0.404` n `8`; equity avg `0.341` n `69`; fx avg `0.0298` n `6`; index avg `0.1774` n `23`; metal avg `-0.0508` n `18`; unknown avg `-0.0034` n `421`
- 24h: commodity avg `-0.2955` n `12`; crypto_alt avg `2.9086` n `228`; crypto_major avg `3.1599` n `8`; equity avg `2.1378` n `69`; fx avg `0.1132` n `6`; index avg `0.3333` n `23`; metal avg `0.0611` n `18`; unknown avg `0.427` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
