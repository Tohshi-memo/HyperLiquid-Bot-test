# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T07:52:17.677832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.2318` n `228`; crypto_major avg `-0.1836` n `8`; equity avg `-0.0831` n `66`; fx avg `-0.0045` n `6`; index avg `0.0134` n `23`; metal avg `-0.0665` n `18`; unknown avg `0.016` n `384`
- 1h: commodity avg `0.0577` n `12`; crypto_alt avg `-0.147` n `228`; crypto_major avg `-0.2279` n `8`; equity avg `0.0269` n `66`; fx avg `-0.0025` n `6`; index avg `0.0243` n `23`; metal avg `-0.1526` n `18`; unknown avg `0.1322` n `384`
- 4h: commodity avg `-0.2608` n `12`; crypto_alt avg `1.06` n `228`; crypto_major avg `0.7858` n `8`; equity avg `0.6057` n `66`; fx avg `-0.0448` n `6`; index avg `0.3443` n `23`; metal avg `0.7883` n `18`; unknown avg `0.2996` n `374`
- 24h: commodity avg `0.1804` n `12`; crypto_alt avg `-0.4798` n `228`; crypto_major avg `-0.4923` n `8`; equity avg `0.0406` n `66`; fx avg `-0.1757` n `6`; index avg `-0.5807` n `23`; metal avg `-1.4373` n `18`; unknown avg `0.1378` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
