# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T11:52:25.150583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.0026` n `8`; equity avg `0.0068` n `114`; fx avg `-0.0015` n `6`; index avg `0.0001` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0679` n `791`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `-0.0065` n `8`; equity avg `-0.032` n `114`; fx avg `-0.0092` n `6`; index avg `0.0011` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0211` n `791`
- 4h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0908` n `230`; crypto_major avg `-0.0703` n `8`; equity avg `-0.0354` n `114`; fx avg `-0.0191` n `6`; index avg `-0.0081` n `25`; metal avg `0.0135` n `20`; unknown avg `0.0836` n `791`
- 24h: commodity avg `0.0243` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.1368` n `8`; equity avg `0.321` n `114`; fx avg `-0.0142` n `6`; index avg `0.051` n `25`; metal avg `0.0337` n `20`; unknown avg `0.1867` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
