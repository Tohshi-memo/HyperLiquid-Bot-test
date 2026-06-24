# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T18:07:51.509080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4439` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.127` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4182` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1291` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `0.2858` n `228`; crypto_major avg `0.2638` n `8`; equity avg `0.0664` n `86`; fx avg `-0.0043` n `6`; index avg `-0.002` n `23`; metal avg `-0.1534` n `20`; unknown avg `0.0616` n `764`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `-0.6019` n `228`; crypto_major avg `-0.6264` n `8`; equity avg `-0.4151` n `86`; fx avg `-0.0014` n `6`; index avg `-0.0874` n `23`; metal avg `-0.5746` n `20`; unknown avg `-0.3691` n `764`
- 4h: commodity avg `0.1706` n `12`; crypto_alt avg `-3.5388` n `228`; crypto_major avg `-3.2733` n `8`; equity avg `-1.1442` n `86`; fx avg `0.0133` n `6`; index avg `-0.1463` n `23`; metal avg `-0.8551` n `20`; unknown avg `-0.4037` n `764`
- 24h: commodity avg `-0.501` n `12`; crypto_alt avg `-4.3514` n `228`; crypto_major avg `-4.091` n `8`; equity avg `1.6877` n `86`; fx avg `0.0652` n `6`; index avg `-0.0303` n `23`; metal avg `-2.1469` n `20`; unknown avg `-0.0944` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
