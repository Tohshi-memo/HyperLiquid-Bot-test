# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T03:37:33.385161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1108` n `12`; crypto_alt avg `-0.0056` n `230`; crypto_major avg `-0.0087` n `8`; equity avg `0.0163` n `108`; fx avg `-0.0013` n `6`; index avg `-0.0168` n `25`; metal avg `0.0028` n `20`; unknown avg `0.0327` n `782`
- 1h: commodity avg `-0.127` n `12`; crypto_alt avg `0.1497` n `230`; crypto_major avg `0.123` n `8`; equity avg `-0.0911` n `108`; fx avg `-0.0101` n `6`; index avg `-0.0287` n `25`; metal avg `-0.1375` n `20`; unknown avg `0.017` n `782`
- 4h: commodity avg `0.0175` n `12`; crypto_alt avg `-0.2571` n `230`; crypto_major avg `-0.6535` n `8`; equity avg `-0.2104` n `108`; fx avg `-0.0493` n `6`; index avg `-0.172` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0915` n `782`
- 24h: commodity avg `0.0727` n `12`; crypto_alt avg `0.0837` n `230`; crypto_major avg `-0.0759` n `8`; equity avg `-1.7834` n `108`; fx avg `-0.005` n `6`; index avg `-0.3454` n `25`; metal avg `0.5329` n `20`; unknown avg `0.978` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
