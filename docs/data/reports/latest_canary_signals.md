# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T19:22:25.207213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.033` n `230`; crypto_major avg `0.0909` n `8`; equity avg `0.0326` n `114`; fx avg `0.0088` n `6`; index avg `0.0028` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0618` n `791`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `-0.311` n `230`; crypto_major avg `-0.1797` n `8`; equity avg `-0.1222` n `114`; fx avg `0.0202` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0157` n `20`; unknown avg `8.6209` n `791`
- 4h: commodity avg `-0.0334` n `12`; crypto_alt avg `0.5836` n `230`; crypto_major avg `-0.0447` n `8`; equity avg `-0.1312` n `114`; fx avg `0.033` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0123` n `20`; unknown avg `18.57` n `791`
- 24h: commodity avg `0.1719` n `12`; crypto_alt avg `0.1017` n `230`; crypto_major avg `-1.1057` n `8`; equity avg `-0.8178` n `114`; fx avg `0.0767` n `6`; index avg `-0.1152` n `25`; metal avg `0.2362` n `20`; unknown avg `0.0289` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
