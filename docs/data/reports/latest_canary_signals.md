# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T19:07:31.316104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.4542` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.2708` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2225` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.057` n `13`; crypto_alt avg `0.1303` n `235`; crypto_major avg `0.0204` n `8`; equity avg `-0.1616` n `150`; fx avg `0.0025` n `6`; index avg `-0.0171` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.2298` n `1075`
- 1h: commodity avg `-0.0949` n `13`; crypto_alt avg `1.8414` n `235`; crypto_major avg `1.4106` n `8`; equity avg `0.0598` n `150`; fx avg `0.0113` n `6`; index avg `0.0335` n `26`; metal avg `0.0001` n `20`; unknown avg `3.3383` n `1075`
- 4h: commodity avg `-0.1271` n `13`; crypto_alt avg `-3.1569` n `235`; crypto_major avg `-2.3979` n `8`; equity avg `-1.453` n `150`; fx avg `-0.0271` n `6`; index avg `-0.1754` n `26`; metal avg `0.0563` n `20`; unknown avg `1.2962` n `1069`
- 24h: commodity avg `0.8141` n `13`; crypto_alt avg `-3.3259` n `235`; crypto_major avg `-4.3101` n `8`; equity avg `-3.1595` n `150`; fx avg `0.065` n `6`; index avg `-0.4076` n `26`; metal avg `0.009` n `20`; unknown avg `23.6137` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
