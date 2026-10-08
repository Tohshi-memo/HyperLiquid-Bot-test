# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T17:37:28.921855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.5277` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.2888` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.2759` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.6516` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0968` n `13`; crypto_alt avg `-0.0134` n `235`; crypto_major avg `0.0751` n `8`; equity avg `0.0232` n `150`; fx avg `-0.0008` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0498` n `20`; unknown avg `0.0818` n `1077`
- 1h: commodity avg `0.0516` n `13`; crypto_alt avg `-1.3807` n `235`; crypto_major avg `-1.0101` n `8`; equity avg `-1.429` n `150`; fx avg `0.0095` n `6`; index avg `-0.224` n `26`; metal avg `0.0873` n `20`; unknown avg `0.0395` n `1075`
- 4h: commodity avg `-0.2596` n `13`; crypto_alt avg `-4.6314` n `235`; crypto_major avg `-3.5355` n `8`; equity avg `-1.8839` n `150`; fx avg `-0.0079` n `6`; index avg `-0.2467` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.5196` n `1021`
- 24h: commodity avg `0.9601` n `13`; crypto_alt avg `-4.5639` n `235`; crypto_major avg `-5.284` n `8`; equity avg `-3.3962` n `150`; fx avg `0.06` n `6`; index avg `-0.4567` n `26`; metal avg `-0.1128` n `20`; unknown avg `23.6107` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
