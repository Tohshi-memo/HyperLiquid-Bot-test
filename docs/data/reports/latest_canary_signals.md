# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T16:52:27.722128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `0.0612` n `235`; crypto_major avg `0.0422` n `8`; equity avg `0.0184` n `144`; fx avg `0.0036` n `6`; index avg `-0.0009` n `26`; metal avg `0.0038` n `20`; unknown avg `0.2381` n `1078`
- 1h: commodity avg `-0.0523` n `13`; crypto_alt avg `0.0929` n `235`; crypto_major avg `0.1251` n `8`; equity avg `0.0295` n `144`; fx avg `-0.0077` n `6`; index avg `-0.0002` n `26`; metal avg `-0.002` n `20`; unknown avg `0.2591` n `1070`
- 4h: commodity avg `-0.1306` n `13`; crypto_alt avg `0.0289` n `235`; crypto_major avg `0.2901` n `8`; equity avg `0.0447` n `144`; fx avg `-0.0005` n `6`; index avg `-0.0209` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.0897` n `1070`
- 24h: commodity avg `-0.1513` n `13`; crypto_alt avg `0.9394` n `235`; crypto_major avg `1.0538` n `8`; equity avg `0.2431` n `144`; fx avg `0.0132` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0062` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
