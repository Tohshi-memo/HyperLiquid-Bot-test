# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T03:22:26.114105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `0.1796` n `238`; crypto_major avg `0.0316` n `8`; equity avg `0.0862` n `156`; fx avg `-0.0067` n `6`; index avg `0.0339` n `27`; metal avg `0.0048` n `20`; unknown avg `0.3343` n `1260`
- 1h: commodity avg `-0.1115` n `13`; crypto_alt avg `0.2395` n `238`; crypto_major avg `0.4277` n `8`; equity avg `0.2009` n `156`; fx avg `-0.0351` n `6`; index avg `0.0168` n `27`; metal avg `-0.0937` n `20`; unknown avg `2.6144` n `1254`
- 4h: commodity avg `0.1528` n `13`; crypto_alt avg `-1.9537` n `238`; crypto_major avg `-0.8994` n `8`; equity avg `-0.4092` n `156`; fx avg `-0.0428` n `6`; index avg `-0.1499` n `27`; metal avg `-0.2967` n `20`; unknown avg `1.7557` n `1238`
- 24h: commodity avg `-0.0403` n `13`; crypto_alt avg `-4.7711` n `238`; crypto_major avg `-0.9095` n `8`; equity avg `-2.6639` n `155`; fx avg `0.1347` n `6`; index avg `-0.2381` n `27`; metal avg `-0.6326` n `20`; unknown avg `29.2635` n `986`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
