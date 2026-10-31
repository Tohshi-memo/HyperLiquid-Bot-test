# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T04:52:25.490178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `-0.1688` n `238`; crypto_major avg `-0.0856` n `8`; equity avg `-0.0393` n `156`; fx avg `-0.0052` n `6`; index avg `0.0006` n `27`; metal avg `-0.0003` n `20`; unknown avg `-0.1317` n `1262`
- 1h: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.4543` n `238`; crypto_major avg `-0.3079` n `8`; equity avg `-0.0891` n `156`; fx avg `-0.0069` n `6`; index avg `-0.0175` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.6918` n `1250`
- 4h: commodity avg `0.1056` n `13`; crypto_alt avg `-1.1924` n `238`; crypto_major avg `-0.8241` n `8`; equity avg `-0.1104` n `156`; fx avg `0.0026` n `6`; index avg `-0.0572` n `27`; metal avg `-0.0203` n `20`; unknown avg `7.6476` n `1234`
- 24h: commodity avg `-0.0134` n `13`; crypto_alt avg `1.2308` n `238`; crypto_major avg `-1.5018` n `8`; equity avg `-2.9831` n `156`; fx avg `-0.0879` n `6`; index avg `-0.2506` n `27`; metal avg `-0.6356` n `20`; unknown avg `2.8433` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
