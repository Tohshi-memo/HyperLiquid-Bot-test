# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:52:24.339844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.3413` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.2589` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.181` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `-0.0642` n `230`; crypto_major avg `-0.1607` n `8`; equity avg `0.0215` n `121`; fx avg `0.0` n `6`; index avg `0.0001` n `25`; metal avg `0.0033` n `20`; unknown avg `0.0436` n `793`
- 1h: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.31` n `230`; crypto_major avg `-0.6204` n `8`; equity avg `0.0116` n `121`; fx avg `0.0013` n `6`; index avg `0.0037` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.1245` n `793`
- 4h: commodity avg `0.0133` n `12`; crypto_alt avg `2.6787` n `230`; crypto_major avg `3.2722` n `8`; equity avg `0.0912` n `121`; fx avg `-0.0046` n `6`; index avg `0.0071` n `25`; metal avg `-0.0691` n `20`; unknown avg `-0.0561` n `793`
- 24h: commodity avg `0.1324` n `12`; crypto_alt avg `8.2907` n `230`; crypto_major avg `7.3244` n `8`; equity avg `1.0722` n `121`; fx avg `-0.0706` n `6`; index avg `0.1702` n `25`; metal avg `0.4351` n `20`; unknown avg `1.3886` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
