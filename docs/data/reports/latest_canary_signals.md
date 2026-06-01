# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T09:22:31.884249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0566` n `12`; crypto_alt avg `0.129` n `228`; crypto_major avg `0.2189` n `8`; equity avg `0.055` n `69`; fx avg `-0.0073` n `6`; index avg `-0.0058` n `23`; metal avg `0.2051` n `18`; unknown avg `0.1725` n `422`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.4058` n `228`; crypto_major avg `0.4087` n `8`; equity avg `0.1785` n `69`; fx avg `-0.007` n `6`; index avg `0.0304` n `23`; metal avg `0.374` n `18`; unknown avg `0.8836` n `422`
- 4h: commodity avg `0.4849` n `12`; crypto_alt avg `-1.2529` n `228`; crypto_major avg `-0.7674` n `8`; equity avg `-0.3117` n `69`; fx avg `-0.0304` n `6`; index avg `-0.1458` n `23`; metal avg `-0.1364` n `18`; unknown avg `0.8115` n `412`
- 24h: commodity avg `1.2944` n `12`; crypto_alt avg `-0.3319` n `228`; crypto_major avg `-0.7536` n `8`; equity avg `-0.1099` n `69`; fx avg `-0.0144` n `6`; index avg `0.5334` n `23`; metal avg `0.2632` n `18`; unknown avg `1.4544` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2877`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
