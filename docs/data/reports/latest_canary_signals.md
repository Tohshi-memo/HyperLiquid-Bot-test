# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T18:37:22.838527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.918` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0516` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.666` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1797` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1158` n `12`; crypto_alt avg `-0.5846` n `228`; crypto_major avg `-0.54` n `8`; equity avg `-0.1291` n `74`; fx avg `-0.0105` n `6`; index avg `0.0851` n `23`; metal avg `0.0105` n `18`; unknown avg `-0.2461` n `424`
- 1h: commodity avg `0.2895` n `12`; crypto_alt avg `-1.9053` n `228`; crypto_major avg `-1.5943` n `8`; equity avg `-1.2579` n `74`; fx avg `-0.008` n `6`; index avg `-0.4146` n `23`; metal avg `-0.5649` n `18`; unknown avg `-0.9281` n `424`
- 4h: commodity avg `-0.4697` n `12`; crypto_alt avg `-3.1389` n `228`; crypto_major avg `-3.3877` n `8`; equity avg `-3.5523` n `74`; fx avg `-0.0962` n `6`; index avg `-1.7217` n `23`; metal avg `-1.3361` n `18`; unknown avg `-1.3537` n `424`
- 24h: commodity avg `-1.3917` n `12`; crypto_alt avg `-9.741` n `228`; crypto_major avg `-8.3227` n `8`; equity avg `-7.1432` n `74`; fx avg `-0.067` n `6`; index avg `-3.8834` n `23`; metal avg `-4.4619` n `18`; unknown avg `-2.237` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
