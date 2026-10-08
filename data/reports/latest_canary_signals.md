# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T18:52:29.225492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.8769` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6992` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1402` n `13`; crypto_alt avg `0.065` n `235`; crypto_major avg `0.1481` n `8`; equity avg `-0.0682` n `150`; fx avg `0.0058` n `6`; index avg `-0.0034` n `26`; metal avg `0.0232` n `20`; unknown avg `-0.155` n `1077`
- 1h: commodity avg `-0.0468` n `13`; crypto_alt avg `1.7133` n `235`; crypto_major avg `1.393` n `8`; equity avg `0.351` n `150`; fx avg `0.0149` n `6`; index avg `0.0738` n `26`; metal avg `0.0236` n `20`; unknown avg `6.9802` n `1075`
- 4h: commodity avg `-0.177` n `13`; crypto_alt avg `-4.0098` n `235`; crypto_major avg `-2.8762` n `8`; equity avg `-1.5642` n `150`; fx avg `-0.0345` n `6`; index avg `-0.1989` n `26`; metal avg `0.0007` n `20`; unknown avg `1.182` n `1069`
- 24h: commodity avg `0.8595` n `13`; crypto_alt avg `-3.6601` n `235`; crypto_major avg `-4.485` n `8`; equity avg `-3.1467` n `150`; fx avg `0.0705` n `6`; index avg `-0.4168` n `26`; metal avg `-0.0769` n `20`; unknown avg `23.4667` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
