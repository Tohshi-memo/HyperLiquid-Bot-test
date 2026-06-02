# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T15:48:27.207825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.18` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `3.2696` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.9173` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.8917` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5421` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.65` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6447` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1259` n `12`; crypto_alt avg `0.6991` n `228`; crypto_major avg `0.3645` n `8`; equity avg `0.0908` n `69`; fx avg `0.011` n `6`; index avg `0.0394` n `23`; metal avg `-0.0198` n `18`; unknown avg `1.1359` n `422`
- 1h: commodity avg `0.1178` n `12`; crypto_alt avg `-1.6975` n `228`; crypto_major avg `-1.4204` n `8`; equity avg `0.0561` n `69`; fx avg `-0.0023` n `6`; index avg `0.2296` n `23`; metal avg `0.2243` n `18`; unknown avg `0.1525` n `422`
- 4h: commodity avg `0.1123` n `12`; crypto_alt avg `-3.232` n `228`; crypto_major avg `-2.7794` n `8`; equity avg `0.1379` n `69`; fx avg `-0.0059` n `6`; index avg `0.4902` n `23`; metal avg `-0.2373` n `18`; unknown avg `-0.3404` n `422`
- 24h: commodity avg `-0.9478` n `12`; crypto_alt avg `-2.6607` n `228`; crypto_major avg `-2.9125` n `8`; equity avg `0.4015` n `69`; fx avg `0.1613` n `6`; index avg `0.8261` n `23`; metal avg `0.9901` n `18`; unknown avg `-0.7741` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
