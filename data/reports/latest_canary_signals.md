# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T16:52:46.518130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2642` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0673` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7832` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0436` n `12`; crypto_alt avg `-0.1313` n `231`; crypto_major avg `0.181` n `8`; equity avg `0.1358` n `127`; fx avg `0.0012` n `6`; index avg `0.0214` n `26`; metal avg `0.0435` n `20`; unknown avg `0.1049` n `792`
- 1h: commodity avg `0.1199` n `12`; crypto_alt avg `0.4784` n `231`; crypto_major avg `0.5053` n `8`; equity avg `0.1743` n `127`; fx avg `0.0122` n `6`; index avg `0.0281` n `26`; metal avg `0.084` n `20`; unknown avg `0.0547` n `792`
- 4h: commodity avg `0.0845` n `12`; crypto_alt avg `1.6127` n `231`; crypto_major avg `2.1518` n `8`; equity avg `-0.1124` n `127`; fx avg `0.0251` n `6`; index avg `0.0324` n `26`; metal avg `0.3686` n `20`; unknown avg `0.1621` n `792`
- 24h: commodity avg `0.0921` n `12`; crypto_alt avg `4.6114` n `231`; crypto_major avg `5.4006` n `8`; equity avg `1.9294` n `127`; fx avg `-0.056` n `6`; index avg `0.252` n `26`; metal avg `0.2358` n `20`; unknown avg `1.0062` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
