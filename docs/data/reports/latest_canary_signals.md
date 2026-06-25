# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T17:07:27.639077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2537` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.934` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.774` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0101` n `228`; crypto_major avg `0.0243` n `8`; equity avg `-0.084` n `86`; fx avg `-0.0039` n `6`; index avg `-0.0021` n `23`; metal avg `0.0115` n `20`; unknown avg `0.1329` n `765`
- 1h: commodity avg `-0.0786` n `12`; crypto_alt avg `-0.8375` n `228`; crypto_major avg `-0.5478` n `8`; equity avg `-0.2796` n `86`; fx avg `0.0042` n `6`; index avg `-0.0272` n `23`; metal avg `-0.0899` n `20`; unknown avg `0.0918` n `765`
- 4h: commodity avg `0.1959` n `12`; crypto_alt avg `-2.556` n `228`; crypto_major avg `-3.0578` n `8`; equity avg `-2.6077` n `86`; fx avg `0.0557` n `6`; index avg `-0.2838` n `23`; metal avg `-0.1238` n `20`; unknown avg `0.9654` n `765`
- 24h: commodity avg `0.2931` n `12`; crypto_alt avg `-0.0211` n `228`; crypto_major avg `-0.4911` n `8`; equity avg `-0.2138` n `86`; fx avg `0.0671` n `6`; index avg `0.383` n `23`; metal avg `0.3339` n `20`; unknown avg `0.3042` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
