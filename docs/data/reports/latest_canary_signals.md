# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T17:37:36.640836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0164` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6176` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.6137` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.1983` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1165` n `12`; crypto_alt avg `-0.1198` n `234`; crypto_major avg `-0.1383` n `8`; equity avg `-0.04` n `141`; fx avg `0.0129` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0344` n `20`; unknown avg `8.3183` n `943`
- 1h: commodity avg `-0.0596` n `12`; crypto_alt avg `-0.0883` n `234`; crypto_major avg `-0.1941` n `8`; equity avg `-0.2516` n `141`; fx avg `0.0208` n `6`; index avg `-0.0532` n `26`; metal avg `-0.1141` n `20`; unknown avg `6.7878` n `933`
- 4h: commodity avg `0.1951` n `12`; crypto_alt avg `-3.555` n `234`; crypto_major avg `-2.8213` n `8`; equity avg `-0.623` n `141`; fx avg `0.0101` n `6`; index avg `-0.2076` n `26`; metal avg `-0.2037` n `20`; unknown avg `1.5508` n `889`
- 24h: commodity avg `0.3646` n `12`; crypto_alt avg `-2.4763` n `234`; crypto_major avg `-3.4752` n `8`; equity avg `-1.2039` n `140`; fx avg `0.03` n `6`; index avg `-0.3266` n `26`; metal avg `-0.6601` n `20`; unknown avg `17.8984` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
