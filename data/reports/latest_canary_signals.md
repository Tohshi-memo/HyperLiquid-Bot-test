# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T06:37:24.463729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `12`; crypto_alt avg `0.1719` n `231`; crypto_major avg `0.1177` n `8`; equity avg `0.0772` n `127`; fx avg `-0.0083` n `6`; index avg `0.0162` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.0488` n `791`
- 1h: commodity avg `-0.0596` n `12`; crypto_alt avg `0.4859` n `231`; crypto_major avg `0.2736` n `8`; equity avg `0.1174` n `127`; fx avg `0.0025` n `6`; index avg `0.0263` n `26`; metal avg `-0.0484` n `20`; unknown avg `0.178` n `775`
- 4h: commodity avg `-0.0896` n `12`; crypto_alt avg `-0.0872` n `231`; crypto_major avg `0.0395` n `8`; equity avg `-0.0545` n `127`; fx avg `0.0067` n `6`; index avg `-0.0701` n `26`; metal avg `-0.1409` n `20`; unknown avg `0.0825` n `775`
- 24h: commodity avg `0.2293` n `12`; crypto_alt avg `0.3867` n `231`; crypto_major avg `0.7124` n `8`; equity avg `1.245` n `127`; fx avg `-0.0906` n `6`; index avg `0.2012` n `26`; metal avg `-0.2577` n `20`; unknown avg `0.3144` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
