# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T14:22:36.709381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.648` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.6353` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.1543` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-3.0046` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.6658` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.6345` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0671` n `12`; crypto_alt avg `0.5722` n `228`; crypto_major avg `0.3713` n `8`; equity avg `0.21` n `86`; fx avg `0.0107` n `6`; index avg `0.0264` n `23`; metal avg `0.0623` n `20`; unknown avg `0.1257` n `765`
- 1h: commodity avg `0.1026` n `12`; crypto_alt avg `-2.4252` n `228`; crypto_major avg `-2.902` n `8`; equity avg `-2.4389` n `86`; fx avg `0.0162` n `6`; index avg `-0.2675` n `23`; metal avg `-0.2362` n `20`; unknown avg `0.239` n `765`
- 4h: commodity avg `0.2632` n `12`; crypto_alt avg `-2.6677` n `228`; crypto_major avg `-3.3848` n `8`; equity avg `-2.4461` n `86`; fx avg `0.0171` n `6`; index avg `-0.2305` n `23`; metal avg `0.2505` n `20`; unknown avg `0.5044` n `765`
- 24h: commodity avg `0.3109` n `12`; crypto_alt avg `-2.557` n `228`; crypto_major avg `-2.7349` n `8`; equity avg `-0.4772` n `86`; fx avg `0.0566` n `6`; index avg `0.3459` n `23`; metal avg `-0.1861` n `20`; unknown avg `-0.4339` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
