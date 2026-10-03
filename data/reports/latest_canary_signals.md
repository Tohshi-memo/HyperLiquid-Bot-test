# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T13:37:25.287916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `13`; crypto_alt avg `0.203` n `235`; crypto_major avg `0.1297` n `8`; equity avg `0.0127` n `143`; fx avg `0.0001` n `6`; index avg `0.0032` n `26`; metal avg `0.0009` n `20`; unknown avg `0.2164` n `984`
- 1h: commodity avg `0.0965` n `13`; crypto_alt avg `0.3224` n `235`; crypto_major avg `0.1148` n `8`; equity avg `-0.0013` n `143`; fx avg `-0.002` n `6`; index avg `0.0058` n `26`; metal avg `0.0008` n `20`; unknown avg `0.3147` n `982`
- 4h: commodity avg `0.0599` n `13`; crypto_alt avg `0.7251` n `235`; crypto_major avg `0.2718` n `8`; equity avg `0.0225` n `143`; fx avg `-0.0137` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.1525` n `972`
- 24h: commodity avg `0.7356` n `13`; crypto_alt avg `-2.8736` n `235`; crypto_major avg `-2.8694` n `8`; equity avg `-0.38` n `143`; fx avg `0.0196` n `6`; index avg `-0.0481` n `26`; metal avg `-0.3659` n `20`; unknown avg `0.0115` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1972`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
