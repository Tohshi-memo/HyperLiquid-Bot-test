# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T08:37:21.743052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `0.0101` n `228`; crypto_major avg `-0.0571` n `8`; equity avg `-0.1185` n `69`; fx avg `-0.0144` n `6`; index avg `-0.0642` n `23`; metal avg `0.0526` n `18`; unknown avg `0.0933` n `422`
- 1h: commodity avg `0.1263` n `12`; crypto_alt avg `-0.3868` n `228`; crypto_major avg `-0.2058` n `8`; equity avg `-0.3305` n `69`; fx avg `-0.0025` n `6`; index avg `-0.6273` n `23`; metal avg `-0.197` n `18`; unknown avg `-0.0976` n `422`
- 4h: commodity avg `0.5291` n `12`; crypto_alt avg `-1.7249` n `228`; crypto_major avg `-0.9852` n `8`; equity avg `-0.5596` n `69`; fx avg `-0.0487` n `6`; index avg `-0.3558` n `23`; metal avg `-0.2401` n `18`; unknown avg `-0.0106` n `412`
- 24h: commodity avg `1.3829` n `12`; crypto_alt avg `-0.6958` n `228`; crypto_major avg `-1.2575` n `8`; equity avg `-0.3994` n `69`; fx avg `-0.0292` n `6`; index avg `0.3913` n `23`; metal avg `-0.0561` n `18`; unknown avg `1.422` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2882`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
