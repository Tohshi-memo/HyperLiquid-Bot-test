# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T14:52:31.304879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6445` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.237` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1842` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-2.1321` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.0769` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.9864` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.7715` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0705` n `12`; crypto_alt avg `-0.1954` n `234`; crypto_major avg `-0.0765` n `8`; equity avg `0.1132` n `140`; fx avg `-0.0192` n `6`; index avg `0.0079` n `26`; metal avg `-0.0078` n `20`; unknown avg `3.0131` n `944`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `-2.6021` n `234`; crypto_major avg `-2.0555` n `8`; equity avg `-0.284` n `140`; fx avg `-0.0158` n `6`; index avg `-0.0691` n `26`; metal avg `0.0766` n `20`; unknown avg `2.0826` n `922`
- 4h: commodity avg `0.1942` n `12`; crypto_alt avg `-3.5326` n `234`; crypto_major avg `-2.4503` n `8`; equity avg `-1.0304` n `140`; fx avg `-0.0071` n `6`; index avg `-0.2133` n `26`; metal avg `-0.2661` n `20`; unknown avg `513.3546` n `898`
- 24h: commodity avg `0.3262` n `12`; crypto_alt avg `0.0155` n `234`; crypto_major avg `-1.9124` n `8`; equity avg `-0.7311` n `140`; fx avg `-0.0036` n `6`; index avg `-0.235` n `26`; metal avg `-0.4547` n `20`; unknown avg `15.0777` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2519`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
