# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T16:22:30.667923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5806` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9588` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7041` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.007` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `0.094` n `92`; fx avg `-0.0071` n `6`; index avg `0.0231` n `25`; metal avg `0.0316` n `20`; unknown avg `0.0101` n `766`
- 1h: commodity avg `0.1494` n `12`; crypto_alt avg `0.0477` n `230`; crypto_major avg `0.1288` n `8`; equity avg `-0.1827` n `92`; fx avg `-0.0077` n `6`; index avg `-0.081` n `25`; metal avg `-0.271` n `20`; unknown avg `-0.1308` n `766`
- 4h: commodity avg `-0.1276` n `12`; crypto_alt avg `1.7264` n `230`; crypto_major avg `2.453` n `8`; equity avg `0.7489` n `92`; fx avg `-0.0392` n `6`; index avg `0.2123` n `25`; metal avg `0.4942` n `20`; unknown avg `0.7373` n `758`
- 24h: commodity avg `0.814` n `12`; crypto_alt avg `1.4327` n `230`; crypto_major avg `3.0719` n `8`; equity avg `0.5922` n `92`; fx avg `-0.0148` n `6`; index avg `0.2355` n `25`; metal avg `0.4596` n `20`; unknown avg `-0.1233` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
