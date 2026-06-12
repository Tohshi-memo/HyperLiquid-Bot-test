# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T15:37:37.366882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2277` n `12`; crypto_alt avg `-0.3661` n `228`; crypto_major avg `-0.4722` n `8`; equity avg `-0.5012` n `74`; fx avg `0.0155` n `6`; index avg `-0.1294` n `23`; metal avg `0.0227` n `18`; unknown avg `-0.0054` n `643`
- 1h: commodity avg `-0.5605` n `12`; crypto_alt avg `-0.0964` n `228`; crypto_major avg `-0.1782` n `8`; equity avg `-0.0633` n `74`; fx avg `0.0022` n `6`; index avg `0.29` n `23`; metal avg `0.7587` n `18`; unknown avg `-0.2809` n `643`
- 4h: commodity avg `0.4212` n `12`; crypto_alt avg `0.221` n `228`; crypto_major avg `0.86` n `8`; equity avg `-0.56` n `74`; fx avg `-0.0018` n `6`; index avg `0.2951` n `23`; metal avg `0.1921` n `18`; unknown avg `13.3219` n `643`
- 24h: commodity avg `-2.0613` n `12`; crypto_alt avg `1.7743` n `228`; crypto_major avg `2.5304` n `8`; equity avg `2.1868` n `74`; fx avg `0.085` n `6`; index avg `1.8262` n `23`; metal avg `2.9509` n `18`; unknown avg `19.714` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
