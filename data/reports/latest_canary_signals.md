# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T07:37:30.700127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6933` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9655` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.1792` n `228`; crypto_major avg `0.3257` n `8`; equity avg `-0.0011` n `86`; fx avg `-0.0002` n `6`; index avg `0.015` n `23`; metal avg `0.0526` n `20`; unknown avg `-0.0165` n `765`
- 1h: commodity avg `-0.1245` n `12`; crypto_alt avg `1.0648` n `228`; crypto_major avg `1.1208` n `8`; equity avg `0.3035` n `86`; fx avg `0.0284` n `6`; index avg `0.035` n `23`; metal avg `0.2544` n `20`; unknown avg `0.1915` n `757`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `2.2481` n `228`; crypto_major avg `2.6958` n `8`; equity avg `1.3032` n `86`; fx avg `-0.0719` n `6`; index avg `0.2489` n `23`; metal avg `0.7303` n `20`; unknown avg `0.4743` n `717`
- 24h: commodity avg `0.1748` n `12`; crypto_alt avg `-1.1879` n `228`; crypto_major avg `-1.343` n `8`; equity avg `-3.6562` n `86`; fx avg `0.0195` n `6`; index avg `-0.5325` n `23`; metal avg `0.7045` n `20`; unknown avg `0.6394` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
