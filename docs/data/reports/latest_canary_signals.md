# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T02:22:28.882417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0855` n `235`; crypto_major avg `0.1287` n `8`; equity avg `0.0314` n `146`; fx avg `-0.002` n `6`; index avg `0.0002` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.0599` n `1077`
- 1h: commodity avg `0.0091` n `13`; crypto_alt avg `-0.4493` n `235`; crypto_major avg `-0.3147` n `8`; equity avg `-0.0453` n `146`; fx avg `-0.028` n `6`; index avg `-0.0158` n `26`; metal avg `-0.0718` n `20`; unknown avg `0.681` n `1075`
- 4h: commodity avg `0.0554` n `13`; crypto_alt avg `-1.3002` n `235`; crypto_major avg `-0.6711` n `8`; equity avg `-0.1276` n `146`; fx avg `-0.008` n `6`; index avg `-0.0544` n `26`; metal avg `-0.1052` n `20`; unknown avg `0.4172` n `1069`
- 24h: commodity avg `-0.031` n `13`; crypto_alt avg `-1.1596` n `235`; crypto_major avg `-0.6742` n `8`; equity avg `-0.0948` n `146`; fx avg `-0.0068` n `6`; index avg `0.0393` n `26`; metal avg `-0.0963` n `20`; unknown avg `628.4558` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
