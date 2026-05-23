# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T02:22:15.310700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `-0.0117` n `228`; crypto_major avg `-0.0544` n `8`; equity avg `0.0077` n `67`; fx avg `-0.001` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.1075` n `386`
- 1h: commodity avg `0.1486` n `12`; crypto_alt avg `0.3377` n `228`; crypto_major avg `-0.0673` n `8`; equity avg `0.0487` n `67`; fx avg `-0.0016` n `6`; index avg `0.0266` n `23`; metal avg `0.0362` n `18`; unknown avg `-0.1567` n `386`
- 4h: commodity avg `0.5418` n `12`; crypto_alt avg `-0.6254` n `228`; crypto_major avg `-0.7509` n `8`; equity avg `-0.4775` n `67`; fx avg `-0.004` n `6`; index avg `-0.1291` n `23`; metal avg `-0.1554` n `18`; unknown avg `-1.0498` n `386`
- 24h: commodity avg `0.0925` n `12`; crypto_alt avg `-3.5016` n `228`; crypto_major avg `-2.8858` n `8`; equity avg `-1.6559` n `67`; fx avg `0.1131` n `6`; index avg `0.0003` n `23`; metal avg `-0.7289` n `18`; unknown avg `-2.122` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
