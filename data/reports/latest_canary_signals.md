# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T11:37:43.447043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `13`; crypto_alt avg `0.0823` n `238`; crypto_major avg `-0.0637` n `8`; equity avg `-0.072` n `156`; fx avg `-0.0114` n `6`; index avg `0.0072` n `27`; metal avg `0.0264` n `20`; unknown avg `0.0243` n `1261`
- 1h: commodity avg `-0.0182` n `13`; crypto_alt avg `0.146` n `238`; crypto_major avg `-0.1092` n `8`; equity avg `-0.4072` n `156`; fx avg `-0.0502` n `6`; index avg `-0.0261` n `27`; metal avg `-0.0378` n `20`; unknown avg `159.3092` n `1255`
- 4h: commodity avg `0.078` n `13`; crypto_alt avg `0.9037` n `238`; crypto_major avg `-0.0112` n `8`; equity avg `-1.0227` n `156`; fx avg `-0.0146` n `6`; index avg `-0.1195` n `27`; metal avg `-0.0626` n `20`; unknown avg `27.0153` n `1190`
- 24h: commodity avg `0.2268` n `13`; crypto_alt avg `-3.4853` n `238`; crypto_major avg `-1.8625` n `8`; equity avg `-4.0401` n `156`; fx avg `0.047` n `6`; index avg `-0.4315` n `27`; metal avg `-0.6798` n `20`; unknown avg `24.0592` n `1034`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
