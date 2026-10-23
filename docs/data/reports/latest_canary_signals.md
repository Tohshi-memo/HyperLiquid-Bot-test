# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T00:37:37.950889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `0.042` n `237`; crypto_major avg `0.1407` n `8`; equity avg `0.2613` n `151`; fx avg `-0.0349` n `6`; index avg `0.0167` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.3305` n `1233`
- 1h: commodity avg `-0.114` n `13`; crypto_alt avg `0.2992` n `237`; crypto_major avg `0.2384` n `8`; equity avg `0.392` n `151`; fx avg `-0.0812` n `6`; index avg `0.0061` n `26`; metal avg `-0.0417` n `20`; unknown avg `0.3701` n `1225`
- 4h: commodity avg `-0.0133` n `13`; crypto_alt avg `0.4245` n `237`; crypto_major avg `0.4087` n `8`; equity avg `-0.0646` n `151`; fx avg `-0.088` n `6`; index avg `-0.0519` n `26`; metal avg `-0.0379` n `20`; unknown avg `0.1632` n `1179`
- 24h: commodity avg `0.4291` n `13`; crypto_alt avg `-4.7172` n `237`; crypto_major avg `-3.3424` n `8`; equity avg `-4.968` n `151`; fx avg `-0.2476` n `6`; index avg `-0.5912` n `26`; metal avg `-1.0374` n `20`; unknown avg `54.3513` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
