# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T04:52:28.544826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.0752` n `230`; crypto_major avg `0.0742` n `8`; equity avg `0.0045` n `114`; fx avg `0.0146` n `6`; index avg `-0.0012` n `25`; metal avg `0.0179` n `20`; unknown avg `16.4853` n `792`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.188` n `230`; crypto_major avg `0.0108` n `8`; equity avg `0.0546` n `114`; fx avg `0.0012` n `6`; index avg `0.0087` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0133` n `792`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `1.0609` n `230`; crypto_major avg `1.2054` n `8`; equity avg `0.6293` n `114`; fx avg `0.0304` n `6`; index avg `0.0701` n `25`; metal avg `0.0429` n `20`; unknown avg `1.4034` n `792`
- 24h: commodity avg `-0.1437` n `12`; crypto_alt avg `0.5223` n `230`; crypto_major avg `0.699` n `8`; equity avg `0.7919` n `114`; fx avg `-0.0205` n `6`; index avg `0.09` n `25`; metal avg `0.1969` n `20`; unknown avg `0.0206` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
