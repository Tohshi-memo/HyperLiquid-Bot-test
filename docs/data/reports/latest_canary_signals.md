# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T10:07:12.343417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.0056` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6063` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `0.2162` n `228`; crypto_major avg `0.1784` n `8`; equity avg `0.0264` n `65`; fx avg `-0.0059` n `5`; index avg `0.0019` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.0171` n `383`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.4071` n `228`; crypto_major avg `0.3752` n `8`; equity avg `0.1203` n `65`; fx avg `-0.0057` n `5`; index avg `0.0432` n `23`; metal avg `-0.0194` n `18`; unknown avg `0.0835` n `383`
- 4h: commodity avg `1.7672` n `12`; crypto_alt avg `-8.6104` n `228`; crypto_major avg `-2.2384` n `8`; equity avg `-2.7188` n `65`; fx avg `-0.1757` n `5`; index avg `-1.7338` n `23`; metal avg `-5.8447` n `18`; unknown avg `550.2045` n `367`
- 24h: commodity avg `1.7672` n `12`; crypto_alt avg `-8.6104` n `228`; crypto_major avg `-2.2384` n `8`; equity avg `-2.7188` n `65`; fx avg `-0.1757` n `5`; index avg `-1.7338` n `23`; metal avg `-5.8447` n `18`; unknown avg `550.2045` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
