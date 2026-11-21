# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T11:46:00.566782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `-0.0299` n `239`; crypto_major avg `0.0057` n `8`; equity avg `-0.0262` n `166`; fx avg `0.0032` n `6`; index avg `-0.0058` n `27`; metal avg `0.0038` n `20`; unknown avg `2.3721` n `1256`
- 1h: commodity avg `0.0303` n `13`; crypto_alt avg `0.285` n `239`; crypto_major avg `0.5441` n `8`; equity avg `0.1972` n `166`; fx avg `0.0267` n `6`; index avg `0.0125` n `27`; metal avg `0.0072` n `20`; unknown avg `2.2614` n `1226`
- 4h: commodity avg `0.0001` n `13`; crypto_alt avg `0.6259` n `239`; crypto_major avg `0.9473` n `8`; equity avg `0.1317` n `166`; fx avg `0.0564` n `6`; index avg `0.0082` n `27`; metal avg `0.0687` n `20`; unknown avg `2.0148` n `1210`
- 24h: commodity avg `0.5103` n `13`; crypto_alt avg `-4.5721` n `239`; crypto_major avg `-5.1083` n `8`; equity avg `-4.0868` n `166`; fx avg `-0.0651` n `6`; index avg `-0.4702` n `27`; metal avg `-0.4132` n `20`; unknown avg `0.0567` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
