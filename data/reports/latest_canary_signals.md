# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T03:22:31.973029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `-0.013` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `0.0302` n `114`; fx avg `-0.0038` n `6`; index avg `-0.0037` n `25`; metal avg `0.0037` n `20`; unknown avg `0.024` n `791`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.1448` n `230`; crypto_major avg `0.0382` n `8`; equity avg `0.0719` n `114`; fx avg `-0.0041` n `6`; index avg `-0.0017` n `25`; metal avg `0.0145` n `20`; unknown avg `-0.0574` n `791`
- 4h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.1191` n `230`; crypto_major avg `0.1018` n `8`; equity avg `0.0874` n `114`; fx avg `0.0013` n `6`; index avg `-0.0009` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.0796` n `791`
- 24h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0742` n `230`; crypto_major avg `-0.1659` n `8`; equity avg `0.2097` n `114`; fx avg `-0.0537` n `6`; index avg `0.0011` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.0663` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
