# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T15:20:00.718017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.0394` n `232`; crypto_major avg `0.0668` n `8`; equity avg `-0.014` n `134`; fx avg `-0.0042` n `6`; index avg `-0.0032` n `26`; metal avg `0.0085` n `20`; unknown avg `0.6749` n `796`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `-0.2772` n `232`; crypto_major avg `-0.2296` n `8`; equity avg `-0.0046` n `134`; fx avg `-0.0024` n `6`; index avg `-0.008` n `26`; metal avg `0.0561` n `20`; unknown avg `0.3931` n `794`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1401` n `232`; crypto_major avg `-0.3868` n `8`; equity avg `0.0013` n `134`; fx avg `-0.0327` n `6`; index avg `0.0211` n `26`; metal avg `0.1836` n `20`; unknown avg `6684.8678` n `748`
- 24h: commodity avg `0.1967` n `12`; crypto_alt avg `1.1655` n `232`; crypto_major avg `-0.5986` n `8`; equity avg `0.4951` n `134`; fx avg `-0.1119` n `6`; index avg `0.0434` n `26`; metal avg `0.0113` n `20`; unknown avg `210.1444` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
