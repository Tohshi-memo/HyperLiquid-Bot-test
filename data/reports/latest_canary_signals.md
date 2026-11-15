# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T19:22:27.667719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `13`; crypto_alt avg `0.2815` n `239`; crypto_major avg `0.3273` n `8`; equity avg `0.1681` n `162`; fx avg `-0.0058` n `6`; index avg `0.0289` n `27`; metal avg `-0.0003` n `20`; unknown avg `1.1708` n `1263`
- 1h: commodity avg `0.0571` n `13`; crypto_alt avg `0.6635` n `239`; crypto_major avg `0.4915` n `8`; equity avg `0.4352` n `162`; fx avg `0.0042` n `6`; index avg `0.0512` n `27`; metal avg `0.0139` n `20`; unknown avg `1.259` n `1261`
- 4h: commodity avg `0.0375` n `13`; crypto_alt avg `0.3` n `239`; crypto_major avg `0.3973` n `8`; equity avg `0.5943` n `162`; fx avg `0.0311` n `6`; index avg `0.0672` n `27`; metal avg `0.0781` n `20`; unknown avg `3.1622` n `1254`
- 24h: commodity avg `0.1086` n `13`; crypto_alt avg `-0.3593` n `239`; crypto_major avg `0.0048` n `8`; equity avg `0.5922` n `162`; fx avg `0.0054` n `6`; index avg `0.0954` n `27`; metal avg `-0.0672` n `20`; unknown avg `3.0766` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
