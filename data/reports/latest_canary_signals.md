# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T14:07:34.517350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-4.102` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-4.0901` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.6595` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-3.381` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.0291` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.9238` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.06` n `12`; crypto_alt avg `0.2978` n `228`; crypto_major avg `0.0311` n `8`; equity avg `0.2196` n `86`; fx avg `-0.0028` n `6`; index avg `0.0405` n `23`; metal avg `0.138` n `20`; unknown avg `0.676` n `765`
- 1h: commodity avg `0.0491` n `12`; crypto_alt avg `-2.9063` n `228`; crypto_major avg `-3.3319` n `8`; equity avg `-2.5916` n `86`; fx avg `0.0023` n `6`; index avg `-0.3028` n `23`; metal avg `-0.4081` n `20`; unknown avg `0.1667` n `765`
- 4h: commodity avg `0.1778` n `12`; crypto_alt avg `-3.3831` n `228`; crypto_major avg `-3.9123` n `8`; equity avg `-2.5994` n `86`; fx avg `-0.0049` n `6`; index avg `-0.2528` n `23`; metal avg `0.1897` n `20`; unknown avg `0.4957` n `765`
- 24h: commodity avg `0.36` n `12`; crypto_alt avg `-3.3236` n `228`; crypto_major avg `-3.4221` n `8`; equity avg `-0.9897` n `86`; fx avg `0.0285` n `6`; index avg `0.3008` n `23`; metal avg `-0.2386` n `20`; unknown avg `-0.5998` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
