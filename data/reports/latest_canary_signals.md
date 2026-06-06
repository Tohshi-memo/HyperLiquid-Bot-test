# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T04:52:20.667327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7228` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.3603` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.119` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0822` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1358` n `12`; crypto_alt avg `0.4623` n `228`; crypto_major avg `0.6638` n `8`; equity avg `0.0247` n `74`; fx avg `-0.0079` n `6`; index avg `-0.073` n `23`; metal avg `-0.0269` n `18`; unknown avg `3.5725` n `425`
- 1h: commodity avg `-0.5313` n `12`; crypto_alt avg `-2.3336` n `228`; crypto_major avg `-1.4861` n `8`; equity avg `-0.7148` n `74`; fx avg `0.014` n `6`; index avg `-0.4039` n `23`; metal avg `-0.2586` n `18`; unknown avg `-0.2065` n `425`
- 4h: commodity avg `-0.368` n `12`; crypto_alt avg `-4.7266` n `228`; crypto_major avg `-3.0908` n `8`; equity avg `-2.0294` n `74`; fx avg `-0.0295` n `6`; index avg `-0.9718` n `23`; metal avg `-0.7305` n `18`; unknown avg `0.3019` n `425`
- 24h: commodity avg `-1.5658` n `12`; crypto_alt avg `-8.4276` n `228`; crypto_major avg `-6.3834` n `8`; equity avg `-7.3007` n `74`; fx avg `-0.1962` n `6`; index avg `-4.444` n `23`; metal avg `-4.4192` n `18`; unknown avg `-0.1193` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
