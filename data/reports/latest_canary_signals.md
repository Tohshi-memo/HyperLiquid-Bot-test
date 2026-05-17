# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T09:58:30.156119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.2031` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.4251` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.1808` n `228`; crypto_major avg `0.2063` n `8`; equity avg `0.0395` n `65`; fx avg `-0.0013` n `5`; index avg `0.0214` n `23`; metal avg `0.0173` n `18`; unknown avg `-0.0344` n `383`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `0.2092` n `228`; crypto_major avg `0.2438` n `8`; equity avg `0.1095` n `65`; fx avg `0.0002` n `5`; index avg `0.0567` n `23`; metal avg `-0.0198` n `18`; unknown avg `0.0395` n `383`
- 4h: commodity avg `1.7908` n `12`; crypto_alt avg `-8.8024` n `228`; crypto_major avg `-2.4123` n `8`; equity avg `-2.7448` n `65`; fx avg `-0.1697` n `5`; index avg `-1.7358` n `23`; metal avg `-5.8374` n `18`; unknown avg `550.2062` n `367`
- 24h: commodity avg `1.7908` n `12`; crypto_alt avg `-8.8024` n `228`; crypto_major avg `-2.4123` n `8`; equity avg `-2.7448` n `65`; fx avg `-0.1697` n `5`; index avg `-1.7358` n `23`; metal avg `-5.8374` n `18`; unknown avg `550.2062` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
