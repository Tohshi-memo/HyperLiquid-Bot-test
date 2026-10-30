# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T07:22:27.797791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6612` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0423` n `13`; crypto_alt avg `-0.2127` n `238`; crypto_major avg `-0.2209` n `8`; equity avg `-0.0593` n `156`; fx avg `-0.0205` n `6`; index avg `0.01` n `27`; metal avg `-0.0121` n `20`; unknown avg `0.0782` n `1258`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `0.0161` n `238`; crypto_major avg `-0.2693` n `8`; equity avg `-0.1366` n `156`; fx avg `-0.0115` n `6`; index avg `0.0359` n `27`; metal avg `-0.0734` n `20`; unknown avg `131.9994` n `1250`
- 4h: commodity avg `-0.0189` n `13`; crypto_alt avg `2.0205` n `238`; crypto_major avg `1.5127` n `8`; equity avg `0.23` n `156`; fx avg `-0.0303` n `6`; index avg `0.1029` n `27`; metal avg `-0.1485` n `20`; unknown avg `8.3498` n `1214`
- 24h: commodity avg `-0.0631` n `13`; crypto_alt avg `-2.8048` n `238`; crypto_major avg `0.248` n `8`; equity avg `-2.7674` n `155`; fx avg `0.1041` n `6`; index avg `-0.3162` n `27`; metal avg `-0.7149` n `20`; unknown avg `30.8887` n `978`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
