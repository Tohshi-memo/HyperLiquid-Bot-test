# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T05:37:21.511108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1599` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.0287` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9163` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6797` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.2965` n `228`; crypto_major avg `-0.3487` n `8`; equity avg `0.0313` n `74`; fx avg `-0.0091` n `6`; index avg `-0.013` n `23`; metal avg `-0.0519` n `18`; unknown avg `-0.5079` n `424`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.0448` n `228`; crypto_major avg `-0.396` n `8`; equity avg `0.3124` n `74`; fx avg `-0.0258` n `6`; index avg `0.1413` n `23`; metal avg `-0.036` n `18`; unknown avg `-0.671` n `424`
- 4h: commodity avg `0.1814` n `12`; crypto_alt avg `-1.8056` n `228`; crypto_major avg `-1.8473` n `8`; equity avg `0.3126` n `74`; fx avg `-0.0508` n `6`; index avg `0.069` n `23`; metal avg `-0.1676` n `18`; unknown avg `-0.2036` n `424`
- 24h: commodity avg `-0.1461` n `12`; crypto_alt avg `-4.4711` n `228`; crypto_major avg `-4.434` n `8`; equity avg `-1.274` n `73`; fx avg `0.1634` n `6`; index avg `-0.445` n `23`; metal avg `-0.5829` n `18`; unknown avg `-0.6031` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
