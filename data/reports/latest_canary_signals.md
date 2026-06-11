# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T20:37:37.286724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0001` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.5387` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `-0.3521` n `228`; crypto_major avg `-0.3893` n `8`; equity avg `-0.07` n `74`; fx avg `0.0054` n `6`; index avg `-0.0631` n `23`; metal avg `-0.0114` n `18`; unknown avg `-0.2986` n `556`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.4989` n `228`; crypto_major avg `-0.9688` n `8`; equity avg `-0.1993` n `74`; fx avg `0.0077` n `6`; index avg `-0.0553` n `23`; metal avg `-0.1514` n `18`; unknown avg `-0.139` n `556`
- 4h: commodity avg `-1.7996` n `12`; crypto_alt avg `0.7504` n `228`; crypto_major avg `1.2005` n `8`; equity avg `1.8515` n `74`; fx avg `0.0652` n `6`; index avg `1.1982` n `23`; metal avg `2.7392` n `18`; unknown avg `-0.0189` n `556`
- 24h: commodity avg `-2.1817` n `12`; crypto_alt avg `3.4269` n `228`; crypto_major avg `3.3033` n `8`; equity avg `3.6729` n `74`; fx avg `0.0426` n `6`; index avg `2.3332` n `23`; metal avg `3.4569` n `18`; unknown avg `2.1037` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
