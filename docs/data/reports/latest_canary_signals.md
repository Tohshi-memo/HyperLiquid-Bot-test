# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T00:52:17.066173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0688` n `12`; crypto_alt avg `0.1001` n `228`; crypto_major avg `-0.0127` n `8`; equity avg `0.0126` n `69`; fx avg `0.0071` n `6`; index avg `0.0024` n `23`; metal avg `0.0226` n `18`; unknown avg `-0.027` n `417`
- 1h: commodity avg `-0.1225` n `12`; crypto_alt avg `0.6881` n `228`; crypto_major avg `0.3676` n `8`; equity avg `0.0164` n `69`; fx avg `0.0572` n `6`; index avg `-0.0466` n `23`; metal avg `0.0144` n `18`; unknown avg `0.4622` n `417`
- 4h: commodity avg `-0.2267` n `12`; crypto_alt avg `0.1411` n `228`; crypto_major avg `0.0669` n `8`; equity avg `0.4764` n `69`; fx avg `0.0689` n `6`; index avg `0.0023` n `23`; metal avg `0.0079` n `18`; unknown avg `-0.2501` n `417`
- 24h: commodity avg `0.381` n `12`; crypto_alt avg `-1.2886` n `228`; crypto_major avg `0.5208` n `8`; equity avg `2.6106` n `69`; fx avg `0.061` n `6`; index avg `0.8418` n `23`; metal avg `0.4748` n `18`; unknown avg `0.1705` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
