# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T18:07:23.868275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.1317` n `230`; crypto_major avg `-0.11` n `8`; equity avg `0.0001` n `114`; fx avg `0.0006` n `6`; index avg `0.0011` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0305` n `791`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `-0.21` n `230`; crypto_major avg `-0.2699` n `8`; equity avg `-0.0029` n `114`; fx avg `-0.0018` n `6`; index avg `-0.0102` n `25`; metal avg `0.0053` n `20`; unknown avg `0.1647` n `791`
- 4h: commodity avg `0.0431` n `12`; crypto_alt avg `-0.1319` n `230`; crypto_major avg `0.0766` n `8`; equity avg `0.1202` n `114`; fx avg `0.0086` n `6`; index avg `-0.0163` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.0394` n `791`
- 24h: commodity avg `0.0694` n `12`; crypto_alt avg `-0.3712` n `230`; crypto_major avg `-0.094` n `8`; equity avg `0.3116` n `114`; fx avg `-0.003` n `6`; index avg `0.0189` n `25`; metal avg `0.0593` n `20`; unknown avg `0.1354` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
