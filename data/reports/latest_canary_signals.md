# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T20:37:40.068545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6681` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.8322` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7703` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0993` n `13`; crypto_alt avg `-0.367` n `239`; crypto_major avg `-0.5869` n `8`; equity avg `-0.438` n `166`; fx avg `-0.0049` n `6`; index avg `-0.0908` n `27`; metal avg `-0.1118` n `20`; unknown avg `170.3191` n `1262`
- 1h: commodity avg `0.245` n `13`; crypto_alt avg `-0.4257` n `239`; crypto_major avg `-0.2962` n `8`; equity avg `-0.73` n `166`; fx avg `-0.0157` n `6`; index avg `-0.1234` n `27`; metal avg `-0.0639` n `20`; unknown avg `172.6098` n `1250`
- 4h: commodity avg `0.5468` n `13`; crypto_alt avg `-1.1969` n `239`; crypto_major avg `-2.1213` n `8`; equity avg `-2.0485` n `166`; fx avg `-0.0146` n `6`; index avg `-0.351` n `27`; metal avg `-0.2891` n `20`; unknown avg `10.8591` n `1247`
- 24h: commodity avg `0.2903` n `13`; crypto_alt avg `-6.3359` n `239`; crypto_major avg `-7.1103` n `8`; equity avg `-8.7181` n `166`; fx avg `-0.0045` n `6`; index avg `-0.9031` n `27`; metal avg `-1.3253` n `20`; unknown avg `45.7318` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
