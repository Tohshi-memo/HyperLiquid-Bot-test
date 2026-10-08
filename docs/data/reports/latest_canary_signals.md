# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T18:07:51.923460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-4.0543` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-4.021` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.8204` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2716` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1047` n `13`; crypto_alt avg `0.0066` n `235`; crypto_major avg `0.0031` n `8`; equity avg `0.1297` n `150`; fx avg `0.0061` n `6`; index avg `0.0231` n `26`; metal avg `0.0287` n `20`; unknown avg `3.9975` n `1075`
- 1h: commodity avg `0.3523` n `13`; crypto_alt avg `-0.7619` n `235`; crypto_major avg `-0.586` n `8`; equity avg `0.0172` n `150`; fx avg `0.0211` n `6`; index avg `0.0009` n `26`; metal avg `-0.0148` n `20`; unknown avg `2.3919` n `1075`
- 4h: commodity avg `-0.0586` n `13`; crypto_alt avg `-5.4891` n `235`; crypto_major avg `-4.0796` n `8`; equity avg `-1.808` n `150`; fx avg `-0.0231` n `6`; index avg `-0.2592` n `26`; metal avg `-0.0253` n `20`; unknown avg `0.9376` n `1045`
- 24h: commodity avg `1.2754` n `13`; crypto_alt avg `-5.1412` n `235`; crypto_major avg `-5.6246` n `8`; equity avg `-3.3395` n `150`; fx avg `0.064` n `6`; index avg `-0.4645` n `26`; metal avg `-0.1124` n `20`; unknown avg `23.5946` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
