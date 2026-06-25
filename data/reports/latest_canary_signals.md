# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T14:52:33.798343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9836` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6564` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3968` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0849` n `12`; crypto_alt avg `0.2702` n `228`; crypto_major avg `0.3294` n `8`; equity avg `0.2622` n `86`; fx avg `-0.0098` n `6`; index avg `0.0442` n `23`; metal avg `0.0635` n `20`; unknown avg `0.5604` n `765`
- 1h: commodity avg `-0.1145` n `12`; crypto_alt avg `1.3946` n `228`; crypto_major avg `0.8082` n `8`; equity avg `0.705` n `86`; fx avg `-0.0074` n `6`; index avg `0.1172` n `23`; metal avg `0.2808` n `20`; unknown avg `1.772` n `765`
- 4h: commodity avg `0.0322` n `12`; crypto_alt avg `-1.9773` n `228`; crypto_major avg `-2.6242` n `8`; equity avg `-2.1853` n `86`; fx avg `0.0061` n `6`; index avg `-0.2274` n `23`; metal avg `0.3594` n `20`; unknown avg `1.3735` n `765`
- 24h: commodity avg `0.1746` n `12`; crypto_alt avg `-2.3497` n `228`; crypto_major avg `-2.5426` n `8`; equity avg `-0.889` n `86`; fx avg `0.0678` n `6`; index avg `0.2747` n `23`; metal avg `0.057` n `20`; unknown avg `0.4987` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
