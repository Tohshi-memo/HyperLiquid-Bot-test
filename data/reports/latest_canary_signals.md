# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T09:07:24.021672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.1151` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.0819` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.849` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.9714` n `228`; crypto_major avg `-0.8489` n `8`; equity avg `-0.3472` n `73`; fx avg `-0.0182` n `6`; index avg `-0.0715` n `23`; metal avg `0.0151` n `18`; unknown avg `0.6297` n `424`
- 1h: commodity avg `-0.2138` n `12`; crypto_alt avg `-0.6681` n `228`; crypto_major avg `-0.6083` n `8`; equity avg `-0.8573` n `73`; fx avg `-0.0166` n `6`; index avg `-0.3629` n `23`; metal avg `0.0402` n `18`; unknown avg `0.5425` n `424`
- 4h: commodity avg `-0.179` n `12`; crypto_alt avg `-1.8323` n `228`; crypto_major avg `-2.2609` n `8`; equity avg `-1.0269` n `73`; fx avg `0.1015` n `6`; index avg `-0.4119` n `23`; metal avg `-0.1458` n `18`; unknown avg `-1.2734` n `404`
- 24h: commodity avg `-0.9317` n `12`; crypto_alt avg `-6.5971` n `228`; crypto_major avg `-5.7906` n `8`; equity avg `-4.4502` n `73`; fx avg `0.0429` n `6`; index avg `-1.4312` n `23`; metal avg `-1.0668` n `18`; unknown avg `-1.3286` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
