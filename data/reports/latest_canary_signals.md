# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T05:37:31.675262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0445` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5811` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0433` n `13`; crypto_alt avg `-0.2138` n `235`; crypto_major avg `-0.1651` n `8`; equity avg `-0.1569` n `151`; fx avg `-0.015` n `6`; index avg `-0.0313` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.0838` n `1135`
- 1h: commodity avg `0.0624` n `13`; crypto_alt avg `0.4164` n `235`; crypto_major avg `0.0627` n `8`; equity avg `0.3211` n `151`; fx avg `0.0261` n `6`; index avg `0.058` n `26`; metal avg `0.023` n `20`; unknown avg `9.9348` n `1129`
- 4h: commodity avg `-0.1833` n `13`; crypto_alt avg `2.4075` n `235`; crypto_major avg `1.8612` n `8`; equity avg `0.5508` n `151`; fx avg `0.0651` n `6`; index avg `0.0382` n `26`; metal avg `0.2801` n `20`; unknown avg `5.4562` n `1091`
- 24h: commodity avg `0.4895` n `13`; crypto_alt avg `-3.9261` n `235`; crypto_major avg `-2.3074` n `8`; equity avg `-3.5496` n `151`; fx avg `0.0117` n `6`; index avg `-0.5047` n `26`; metal avg `-0.0182` n `20`; unknown avg `0.5242` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1996`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1869`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1363`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `666`, weak_sample_signal
