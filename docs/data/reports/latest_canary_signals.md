# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T08:22:23.582440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `-0.0132` n `238`; crypto_major avg `-0.0453` n `8`; equity avg `0.0126` n `156`; fx avg `0.0082` n `6`; index avg `0.0002` n `27`; metal avg `-0.001` n `20`; unknown avg `0.1667` n `1262`
- 1h: commodity avg `-0.0406` n `13`; crypto_alt avg `-0.3629` n `238`; crypto_major avg `-0.2493` n `8`; equity avg `-0.0564` n `156`; fx avg `0.0105` n `6`; index avg `0.0023` n `27`; metal avg `-0.0199` n `20`; unknown avg `202.8168` n `1238`
- 4h: commodity avg `-0.0525` n `13`; crypto_alt avg `-0.6769` n `238`; crypto_major avg `-0.4571` n `8`; equity avg `-0.0856` n `156`; fx avg `0.0126` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0062` n `20`; unknown avg `0.8921` n `1210`
- 24h: commodity avg `-0.1572` n `13`; crypto_alt avg `0.4312` n `238`; crypto_major avg `-1.2899` n `8`; equity avg `-1.9993` n `156`; fx avg `-0.0586` n `6`; index avg `-0.2005` n `27`; metal avg `-0.4653` n `20`; unknown avg `4.775` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
