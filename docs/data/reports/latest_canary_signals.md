# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T20:07:16.009365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `-0.1168` n `228`; crypto_major avg `-0.0595` n `8`; equity avg `0.0443` n `66`; fx avg `-0.0639` n `6`; index avg `0.0113` n `23`; metal avg `-0.0552` n `18`; unknown avg `-0.1357` n `384`
- 1h: commodity avg `0.0482` n `12`; crypto_alt avg `0.4104` n `228`; crypto_major avg `0.4556` n `8`; equity avg `0.1429` n `66`; fx avg `-0.0656` n `6`; index avg `0.0941` n `23`; metal avg `-0.0669` n `18`; unknown avg `-0.0285` n `384`
- 4h: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0658` n `228`; crypto_major avg `0.0926` n `8`; equity avg `0.0843` n `66`; fx avg `-0.0403` n `6`; index avg `0.1531` n `23`; metal avg `0.1079` n `18`; unknown avg `0.4793` n `384`
- 24h: commodity avg `-2.5719` n `12`; crypto_alt avg `2.8031` n `228`; crypto_major avg `1.9535` n `8`; equity avg `1.7131` n `66`; fx avg `-0.113` n `6`; index avg `1.1367` n `23`; metal avg `1.7052` n `18`; unknown avg `0.9667` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
