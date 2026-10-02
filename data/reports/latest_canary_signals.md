# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T10:37:29.972881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `13`; crypto_alt avg `0.1253` n `234`; crypto_major avg `0.174` n `8`; equity avg `0.0579` n `142`; fx avg `-0.0042` n `6`; index avg `0.0269` n `26`; metal avg `0.0889` n `20`; unknown avg `-0.2738` n `985`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `0.0436` n `234`; crypto_major avg `0.247` n `8`; equity avg `-0.1022` n `142`; fx avg `-0.0187` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0657` n `20`; unknown avg `0.1254` n `981`
- 4h: commodity avg `-0.5009` n `13`; crypto_alt avg `0.4765` n `234`; crypto_major avg `0.5431` n `8`; equity avg `0.4143` n `142`; fx avg `-0.0609` n `6`; index avg `0.0985` n `26`; metal avg `-0.074` n `20`; unknown avg `-0.5937` n `907`
- 24h: commodity avg `-0.6376` n `13`; crypto_alt avg `2.0121` n `234`; crypto_major avg `2.2507` n `8`; equity avg `1.0464` n `142`; fx avg `-0.3299` n `6`; index avg `0.189` n `26`; metal avg `0.0398` n `20`; unknown avg `-0.1261` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
