# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T05:07:30.412857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8899` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4948` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4876` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.2807` n `235`; crypto_major avg `0.0936` n `8`; equity avg `0.1562` n `151`; fx avg `0.0149` n `6`; index avg `0.0482` n `26`; metal avg `0.0213` n `20`; unknown avg `2.3483` n `1131`
- 1h: commodity avg `0.0697` n `13`; crypto_alt avg `0.7589` n `235`; crypto_major avg `0.2563` n `8`; equity avg `-0.0888` n `151`; fx avg `0.0015` n `6`; index avg `0.0125` n `26`; metal avg `0.055` n `20`; unknown avg `2.0811` n `1129`
- 4h: commodity avg `-0.1704` n `13`; crypto_alt avg `3.5347` n `235`; crypto_major avg `2.7195` n `8`; equity avg `0.2319` n `151`; fx avg `0.0691` n `6`; index avg `-0.0476` n `26`; metal avg `0.2247` n `20`; unknown avg `6.9094` n `1091`
- 24h: commodity avg `0.5478` n `13`; crypto_alt avg `-4.335` n `235`; crypto_major avg `-2.6797` n `8`; equity avg `-3.8628` n `151`; fx avg `0.0017` n `6`; index avg `-0.5636` n `26`; metal avg `-0.0368` n `20`; unknown avg `0.5358` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2034`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1916`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1365`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0829`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `666`, weak_sample_signal
