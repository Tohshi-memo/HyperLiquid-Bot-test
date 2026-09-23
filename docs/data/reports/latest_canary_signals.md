# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T16:52:37.728980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8484` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5733` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5632` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9579` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.077` n `12`; crypto_alt avg `-0.3112` n `234`; crypto_major avg `-0.4715` n `8`; equity avg `-0.2571` n `141`; fx avg `-0.0075` n `6`; index avg `-0.0559` n `26`; metal avg `-0.0975` n `20`; unknown avg `0.1476` n `943`
- 1h: commodity avg `-0.0979` n `12`; crypto_alt avg `0.156` n `234`; crypto_major avg `-0.2349` n `8`; equity avg `-0.1389` n `141`; fx avg `-0.0243` n `6`; index avg `-0.0502` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.2887` n `929`
- 4h: commodity avg `0.0531` n `12`; crypto_alt avg `-3.8822` n `234`; crypto_major avg `-2.7953` n `8`; equity avg `-0.8374` n `141`; fx avg `-0.0348` n `6`; index avg `-0.2321` n `26`; metal avg `-0.222` n `20`; unknown avg `513.659` n `891`
- 24h: commodity avg `0.2757` n `12`; crypto_alt avg `-2.3803` n `234`; crypto_major avg `-3.5271` n `8`; equity avg `-1.135` n `140`; fx avg `0.0111` n `6`; index avg `-0.3345` n `26`; metal avg `-0.6486` n `20`; unknown avg `14.623` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2594`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
