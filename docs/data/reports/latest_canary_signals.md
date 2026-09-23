# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T17:22:36.890541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4833` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2054` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1714` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0441` n `12`; crypto_alt avg `0.6801` n `234`; crypto_major avg `0.6154` n `8`; equity avg `0.2194` n `141`; fx avg `0.015` n `6`; index avg `0.0289` n `26`; metal avg `0.0105` n `20`; unknown avg `2.5952` n `935`
- 1h: commodity avg `-0.1607` n `12`; crypto_alt avg `0.0529` n `234`; crypto_major avg `-0.0927` n `8`; equity avg `-0.1301` n `141`; fx avg `-0.0027` n `6`; index avg `-0.0409` n `26`; metal avg `-0.0449` n `20`; unknown avg `-0.0231` n `933`
- 4h: commodity avg `0.0796` n `12`; crypto_alt avg `-3.3417` n `234`; crypto_major avg `-2.4037` n `8`; equity avg `-0.9839` n `141`; fx avg `-0.0148` n `6`; index avg `-0.2323` n `26`; metal avg `-0.1983` n `20`; unknown avg `1.4013` n `889`
- 24h: commodity avg `0.2056` n `12`; crypto_alt avg `-2.4048` n `234`; crypto_major avg `-3.3741` n `8`; equity avg `-1.1532` n `140`; fx avg `0.0091` n `6`; index avg `-0.3147` n `26`; metal avg `-0.6217` n `20`; unknown avg `12.1454` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2608`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
