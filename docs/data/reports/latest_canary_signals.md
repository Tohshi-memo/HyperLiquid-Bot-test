# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T09:22:37.821996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.1004` n `238`; crypto_major avg `-0.0612` n `8`; equity avg `0.0172` n `156`; fx avg `-0.0054` n `6`; index avg `-0.006` n `27`; metal avg `0.0054` n `20`; unknown avg `-0.1015` n `1262`
- 1h: commodity avg `0.0311` n `13`; crypto_alt avg `0.1102` n `238`; crypto_major avg `0.0243` n `8`; equity avg `0.0263` n `156`; fx avg `-0.0112` n `6`; index avg `-0.0063` n `27`; metal avg `0.0168` n `20`; unknown avg `-0.106` n `1256`
- 4h: commodity avg `0.0222` n `13`; crypto_alt avg `0.0284` n `238`; crypto_major avg `-0.1817` n `8`; equity avg `-0.0203` n `156`; fx avg `0.0095` n `6`; index avg `-0.0017` n `27`; metal avg `0.0036` n `20`; unknown avg `0.5872` n `1212`
- 24h: commodity avg `-0.1676` n `13`; crypto_alt avg `0.8851` n `238`; crypto_major avg `-0.7577` n `8`; equity avg `-1.9198` n `156`; fx avg `-0.103` n `6`; index avg `-0.2083` n `27`; metal avg `-0.4949` n `20`; unknown avg `4.6268` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
