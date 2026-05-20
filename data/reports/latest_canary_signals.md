# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T23:37:13.858536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `0.1558` n `228`; crypto_major avg `0.1591` n `8`; equity avg `-0.0891` n `66`; fx avg `0.008` n `6`; index avg `-0.0309` n `23`; metal avg `0.0877` n `18`; unknown avg `0.399` n `384`
- 1h: commodity avg `-0.354` n `12`; crypto_alt avg `0.1281` n `228`; crypto_major avg `0.1147` n `8`; equity avg `0.015` n `66`; fx avg `-0.0015` n `6`; index avg `-0.0002` n `23`; metal avg `0.0554` n `18`; unknown avg `0.4799` n `384`
- 4h: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.2831` n `228`; crypto_major avg `0.2237` n `8`; equity avg `-0.2787` n `66`; fx avg `-0.063` n `6`; index avg `-0.3047` n `23`; metal avg `-0.2508` n `18`; unknown avg `-0.0106` n `384`
- 24h: commodity avg `-2.3393` n `12`; crypto_alt avg `2.7198` n `228`; crypto_major avg `2.1654` n `8`; equity avg `1.2005` n `66`; fx avg `-0.0634` n `6`; index avg `0.8238` n `23`; metal avg `1.1356` n `18`; unknown avg `1.1002` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
