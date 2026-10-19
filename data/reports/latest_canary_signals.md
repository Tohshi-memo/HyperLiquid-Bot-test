# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T01:37:25.644414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8213` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0848` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0577` n `13`; crypto_alt avg `0.1114` n `237`; crypto_major avg `-0.0216` n `8`; equity avg `-0.0507` n `151`; fx avg `-0.0281` n `6`; index avg `-0.0271` n `26`; metal avg `0.0307` n `20`; unknown avg `-0.0161` n `1194`
- 1h: commodity avg `0.0272` n `13`; crypto_alt avg `0.5595` n `237`; crypto_major avg `0.3531` n `8`; equity avg `0.6998` n `151`; fx avg `-0.0329` n `6`; index avg `0.1326` n `26`; metal avg `0.0366` n `20`; unknown avg `0.4128` n `1156`
- 4h: commodity avg `-0.4557` n `13`; crypto_alt avg `3.3576` n `237`; crypto_major avg `2.3656` n `8`; equity avg `2.7039` n `151`; fx avg `0.0347` n `6`; index avg `0.5175` n `26`; metal avg `0.2808` n `20`; unknown avg `5.764` n `1078`
- 24h: commodity avg `-0.3171` n `13`; crypto_alt avg `-0.3415` n `237`; crypto_major avg `0.6353` n `8`; equity avg `2.1511` n `151`; fx avg `-0.022` n `6`; index avg `0.4268` n `26`; metal avg `0.2335` n `20`; unknown avg `2.1701` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2014`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0616`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
