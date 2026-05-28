# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T22:22:20.111419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0679` n `12`; crypto_alt avg `-0.3` n `228`; crypto_major avg `-0.2446` n `8`; equity avg `0.104` n `69`; fx avg `-0.001` n `6`; index avg `0.0258` n `23`; metal avg `-0.1003` n `18`; unknown avg `-0.0259` n `417`
- 1h: commodity avg `0.2384` n `12`; crypto_alt avg `-0.5844` n `228`; crypto_major avg `-0.3851` n `8`; equity avg `0.2826` n `69`; fx avg `-0.0137` n `6`; index avg `0.0725` n `23`; metal avg `-0.0237` n `18`; unknown avg `-0.132` n `417`
- 4h: commodity avg `0.1762` n `12`; crypto_alt avg `-0.6685` n `228`; crypto_major avg `-0.2977` n `8`; equity avg `0.3488` n `69`; fx avg `-0.0077` n `6`; index avg `-0.1676` n `23`; metal avg `-0.1923` n `18`; unknown avg `0.1353` n `417`
- 24h: commodity avg `0.9767` n `12`; crypto_alt avg `-2.1775` n `228`; crypto_major avg `-0.2525` n `8`; equity avg `2.2522` n `69`; fx avg `-0.0191` n `6`; index avg `0.7773` n `23`; metal avg `0.3561` n `18`; unknown avg `-0.1088` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
