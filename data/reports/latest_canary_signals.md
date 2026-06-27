# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T17:22:29.991814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.0884` n `228`; crypto_major avg `-0.0381` n `8`; equity avg `-0.0055` n `88`; fx avg `0.0006` n `6`; index avg `-0.0005` n `23`; metal avg `-0.027` n `20`; unknown avg `-0.0606` n `764`
- 1h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.5421` n `228`; crypto_major avg `-0.4922` n `8`; equity avg `-0.1119` n `88`; fx avg `-0.0061` n `6`; index avg `-0.0277` n `23`; metal avg `-0.0304` n `20`; unknown avg `0.127` n `764`
- 4h: commodity avg `-0.1532` n `12`; crypto_alt avg `0.1504` n `228`; crypto_major avg `0.0719` n `8`; equity avg `-0.1016` n `88`; fx avg `0.0025` n `6`; index avg `-0.0313` n `23`; metal avg `-0.0277` n `20`; unknown avg `0.0472` n `764`
- 24h: commodity avg `0.1755` n `12`; crypto_alt avg `-0.0585` n `228`; crypto_major avg `-0.0309` n `8`; equity avg `0.2703` n `87`; fx avg `0.0729` n `6`; index avg `-0.1483` n `23`; metal avg `-0.0484` n `20`; unknown avg `0.1178` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
