# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T13:52:37.768143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.1275` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.9509` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.6755` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-3.4302` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-3.0316` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `3.0073` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `-2.841` n `228`; crypto_major avg `-2.8008` n `8`; equity avg `-2.0805` n `86`; fx avg `0.0101` n `6`; index avg `-0.3066` n `23`; metal avg `-0.3291` n `20`; unknown avg `-0.3962` n `765`
- 1h: commodity avg `0.0583` n `12`; crypto_alt avg `-3.1345` n `228`; crypto_major avg `-3.3719` n `8`; equity avg `-2.9542` n `86`; fx avg `0.0134` n `6`; index avg `-0.3646` n `23`; metal avg `-0.3403` n `20`; unknown avg `-0.2838` n `765`
- 4h: commodity avg `0.1546` n `12`; crypto_alt avg `-3.6908` n `228`; crypto_major avg `-3.9729` n `8`; equity avg `-2.7526` n `86`; fx avg `-0.0189` n `6`; index avg `-0.2974` n `23`; metal avg `-0.022` n `20`; unknown avg `-0.0795` n `765`
- 24h: commodity avg `0.2034` n `12`; crypto_alt avg `-3.4881` n `228`; crypto_major avg `-3.5289` n `8`; equity avg `-1.5434` n `86`; fx avg `0.0358` n `6`; index avg `0.2076` n `23`; metal avg `-0.4795` n `20`; unknown avg `-0.8019` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
