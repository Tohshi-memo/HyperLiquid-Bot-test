# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T01:37:27.925530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.257` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9019` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.8432` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.93` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1605` n `13`; crypto_alt avg `0.254` n `238`; crypto_major avg `0.1886` n `8`; equity avg `0.3689` n `156`; fx avg `-0.0187` n `6`; index avg `0.0147` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.1262` n `1260`
- 1h: commodity avg `0.1427` n `13`; crypto_alt avg `0.559` n `238`; crypto_major avg `0.0667` n `8`; equity avg `-0.441` n `156`; fx avg `-0.0173` n `6`; index avg `-0.127` n `27`; metal avg `-0.1945` n `20`; unknown avg `0.7193` n `1254`
- 4h: commodity avg `0.1508` n `13`; crypto_alt avg `-3.9008` n `238`; crypto_major avg `-3.1062` n `8`; equity avg `-1.1762` n `156`; fx avg `0.0161` n `6`; index avg `-0.2043` n `27`; metal avg `-0.263` n `20`; unknown avg `6.316` n `1240`
- 24h: commodity avg `-0.15` n `13`; crypto_alt avg `-6.9735` n `238`; crypto_major avg `-3.0591` n `8`; equity avg `-3.6569` n `155`; fx avg `0.1942` n `6`; index avg `-0.3574` n `27`; metal avg `-0.7936` n `20`; unknown avg `32.6768` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
