# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T08:37:14.942375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.4742` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.125` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0672` n `12`; crypto_alt avg `0.0558` n `228`; crypto_major avg `-0.0151` n `8`; equity avg `0.0015` n `65`; fx avg `0.0009` n `5`; index avg `0.0143` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.0028` n `383`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0802` n `228`; crypto_major avg `-0.1813` n `8`; equity avg `-0.0252` n `65`; fx avg `-0.0042` n `5`; index avg `0.02` n `23`; metal avg `-0.01` n `18`; unknown avg `-0.0408` n `383`
- 4h: commodity avg `1.7874` n `12`; crypto_alt avg `-8.8953` n `228`; crypto_major avg `-2.6868` n `8`; equity avg `-2.8878` n `65`; fx avg `-0.1708` n `5`; index avg `-1.784` n `23`; metal avg `-5.8118` n `18`; unknown avg `550.129` n `367`
- 24h: commodity avg `1.7874` n `12`; crypto_alt avg `-8.8953` n `228`; crypto_major avg `-2.6868` n `8`; equity avg `-2.8878` n `65`; fx avg `-0.1708` n `5`; index avg `-1.784` n `23`; metal avg `-5.8118` n `18`; unknown avg `550.129` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
