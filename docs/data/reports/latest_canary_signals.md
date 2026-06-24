# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T16:52:27.346209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.628` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.6061` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.5021` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1156` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-1.7331` n `228`; crypto_major avg `-0.9402` n `8`; equity avg `-0.1137` n `86`; fx avg `-0.0022` n `6`; index avg `-0.0243` n `23`; metal avg `-0.1305` n `20`; unknown avg `-0.6074` n `764`
- 1h: commodity avg `0.0817` n `12`; crypto_alt avg `-1.8272` n `228`; crypto_major avg `-0.9896` n `8`; equity avg `-0.5991` n `86`; fx avg `0.0115` n `6`; index avg `-0.062` n `23`; metal avg `-0.1136` n `20`; unknown avg `-0.1253` n `764`
- 4h: commodity avg `-0.0484` n `12`; crypto_alt avg `-4.0053` n `228`; crypto_major avg `-3.6764` n `8`; equity avg `-1.5608` n `86`; fx avg `0.0218` n `6`; index avg `-0.0703` n `23`; metal avg `-0.1743` n `20`; unknown avg `1.0075` n `764`
- 24h: commodity avg `-0.3318` n `12`; crypto_alt avg `-4.1129` n `228`; crypto_major avg `-3.6534` n `8`; equity avg `1.997` n `86`; fx avg `0.0514` n `6`; index avg `0.0178` n `23`; metal avg `-1.6714` n `20`; unknown avg `0.1259` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
