# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T14:07:29.238506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1317` n `12`; crypto_alt avg `-0.3558` n `234`; crypto_major avg `-0.4677` n `8`; equity avg `-0.0318` n `141`; fx avg `-0.0073` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0056` n `20`; unknown avg `1.4192` n `961`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.272` n `234`; crypto_major avg `-0.485` n `8`; equity avg `-0.0343` n `141`; fx avg `0.0131` n `6`; index avg `-0.0438` n `26`; metal avg `-0.0011` n `20`; unknown avg `20.2608` n `961`
- 4h: commodity avg `-0.2287` n `12`; crypto_alt avg `0.4489` n `234`; crypto_major avg `0.1631` n `8`; equity avg `0.2802` n `141`; fx avg `-0.0357` n `6`; index avg `0.0121` n `26`; metal avg `-0.0315` n `20`; unknown avg `2.2376` n `955`
- 24h: commodity avg `-0.6538` n `12`; crypto_alt avg `1.4499` n `234`; crypto_major avg `0.5929` n `8`; equity avg `0.2907` n `141`; fx avg `-0.0957` n `6`; index avg `-0.0131` n `26`; metal avg `-0.1398` n `20`; unknown avg `2.2833` n `804`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
