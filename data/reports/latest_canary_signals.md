# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T06:52:22.330380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.016` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0011` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.833` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.3667` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.9343` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.7936` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.2831` n `228`; crypto_major avg `-0.1409` n `8`; equity avg `0.0625` n `74`; fx avg `-0.0038` n `6`; index avg `-0.0287` n `23`; metal avg `0.1561` n `18`; unknown avg `0.0499` n `424`
- 1h: commodity avg `-0.1062` n `12`; crypto_alt avg `-2.945` n `228`; crypto_major avg `-1.8083` n `8`; equity avg `-0.5101` n `74`; fx avg `-0.0198` n `6`; index avg `-0.0147` n `23`; metal avg `0.126` n `18`; unknown avg `0.2129` n `404`
- 4h: commodity avg `-0.2472` n `12`; crypto_alt avg `-3.4732` n `228`; crypto_major avg `-3.0802` n `8`; equity avg `-0.7135` n `74`; fx avg `-0.024` n `6`; index avg `-0.0791` n `23`; metal avg `-0.0642` n `18`; unknown avg `-0.2484` n `404`
- 24h: commodity avg `-0.2484` n `12`; crypto_alt avg `-8.1559` n `228`; crypto_major avg `-6.4512` n `8`; equity avg `-2.0497` n `73`; fx avg `0.1411` n `6`; index avg `-0.5885` n `23`; metal avg `-0.3242` n `18`; unknown avg `-1.31` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
