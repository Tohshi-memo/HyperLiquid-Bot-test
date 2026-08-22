# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T10:22:24.575750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5308` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.5164` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.3381` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.3123` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.3111` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.2958` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-2.1311` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-1.113` n `230`; crypto_major avg `-0.9905` n `8`; equity avg `-0.1066` n `121`; fx avg `0.0041` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.2327` n `794`
- 1h: commodity avg `-0.0232` n `12`; crypto_alt avg `-2.3651` n `230`; crypto_major avg `-2.319` n `8`; equity avg `-0.1879` n `121`; fx avg `0.0042` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0827` n `794`
- 4h: commodity avg `-0.0378` n `12`; crypto_alt avg `-2.547` n `230`; crypto_major avg `-2.5542` n `8`; equity avg `-0.2161` n `121`; fx avg `0.0029` n `6`; index avg `-0.0234` n `25`; metal avg `0.0243` n `20`; unknown avg `0.5564` n `794`
- 24h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.6043` n `230`; crypto_major avg `1.3351` n `8`; equity avg `-1.1003` n `121`; fx avg `0.0449` n `6`; index avg `-0.1061` n `25`; metal avg `-0.081` n `20`; unknown avg `1.3355` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
