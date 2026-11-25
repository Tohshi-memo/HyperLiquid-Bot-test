# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T06:22:28.029548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0587` n `13`; crypto_alt avg `0.4658` n `239`; crypto_major avg `0.1979` n `8`; equity avg `0.148` n `168`; fx avg `0.0035` n `6`; index avg `0.0162` n `27`; metal avg `0.0943` n `20`; unknown avg `0.4401` n `1265`
- 1h: commodity avg `0.1051` n `13`; crypto_alt avg `0.4058` n `239`; crypto_major avg `0.1795` n `8`; equity avg `-0.0465` n `168`; fx avg `0.0055` n `6`; index avg `0.0064` n `27`; metal avg `-0.1418` n `20`; unknown avg `204.2566` n `1233`
- 4h: commodity avg `0.0078` n `13`; crypto_alt avg `1.3663` n `239`; crypto_major avg `0.3115` n `8`; equity avg `-0.4766` n `168`; fx avg `-0.0514` n `6`; index avg `0.0342` n `27`; metal avg `-0.4504` n `20`; unknown avg `205.9421` n `1223`
- 24h: commodity avg `0.562` n `13`; crypto_alt avg `-2.8905` n `239`; crypto_major avg `-3.0408` n `8`; equity avg `-5.2323` n `167`; fx avg `0.1299` n `6`; index avg `-0.4859` n `27`; metal avg `-0.9816` n `20`; unknown avg `696.4852` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
