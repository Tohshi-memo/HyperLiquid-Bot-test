# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T05:07:25.400839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.783` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3612` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0554` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0043` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.1381` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.056` n `12`; crypto_alt avg `-0.8703` n `228`; crypto_major avg `-0.9476` n `8`; equity avg `-0.1543` n `74`; fx avg `-0.001` n `6`; index avg `-0.0432` n `23`; metal avg `-0.0566` n `18`; unknown avg `0.1741` n `425`
- 1h: commodity avg `-0.1932` n `12`; crypto_alt avg `-2.3317` n `228`; crypto_major avg `-1.6988` n `8`; equity avg `-0.7841` n `74`; fx avg `-0.0082` n `6`; index avg `-0.5607` n `23`; metal avg `-0.2471` n `18`; unknown avg `0.7618` n `425`
- 4h: commodity avg `-0.378` n `12`; crypto_alt avg `-5.5558` n `228`; crypto_major avg `-4.161` n `8`; equity avg `-2.1567` n `74`; fx avg `-0.0225` n `6`; index avg `-1.1056` n `23`; metal avg `-0.7998` n `18`; unknown avg `0.391` n `425`
- 24h: commodity avg `-1.5448` n `12`; crypto_alt avg `-9.5605` n `228`; crypto_major avg `-7.7418` n `8`; equity avg `-7.5221` n `74`; fx avg `-0.1919` n `6`; index avg `-4.5177` n `23`; metal avg `-4.5543` n `18`; unknown avg `-1.4556` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
