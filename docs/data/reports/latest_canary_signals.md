# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T05:12:08.441239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.3314` n `234`; crypto_major avg `0.2995` n `8`; equity avg `0.0303` n `140`; fx avg `-0.0005` n `6`; index avg `-0.0075` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.1115` n `940`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `-0.5317` n `234`; crypto_major avg `-0.2028` n `8`; equity avg `-0.0447` n `140`; fx avg `-0.0109` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0817` n `940`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.13` n `234`; crypto_major avg `-0.1481` n `8`; equity avg `-0.1599` n `140`; fx avg `0.0048` n `6`; index avg `-0.0298` n `26`; metal avg `0.0063` n `20`; unknown avg `0.5337` n `914`
- 24h: commodity avg `0.0933` n `12`; crypto_alt avg `3.8275` n `234`; crypto_major avg `4.581` n `8`; equity avg `0.527` n `140`; fx avg `0.0044` n `6`; index avg `0.0022` n `26`; metal avg `0.0285` n `20`; unknown avg `2.4034` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
