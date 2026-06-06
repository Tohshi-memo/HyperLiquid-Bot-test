# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T08:52:21.747233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9116` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5087` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3802` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `0.1418` n `228`; crypto_major avg `0.1299` n `8`; equity avg `0.1498` n `74`; fx avg `0.0` n `6`; index avg `0.1756` n `23`; metal avg `0.0281` n `18`; unknown avg `0.2613` n `425`
- 1h: commodity avg `0.1143` n `12`; crypto_alt avg `0.7767` n `228`; crypto_major avg `0.6132` n `8`; equity avg `0.2573` n `74`; fx avg `-0.0025` n `6`; index avg `0.1935` n `23`; metal avg `0.0747` n `18`; unknown avg `0.4392` n `425`
- 4h: commodity avg `-0.0011` n `12`; crypto_alt avg `3.7133` n `228`; crypto_major avg `2.9105` n `8`; equity avg `0.5303` n `74`; fx avg `-0.0131` n `6`; index avg `0.3954` n `23`; metal avg `0.4018` n `18`; unknown avg `0.8211` n `415`
- 24h: commodity avg `-1.2956` n `12`; crypto_alt avg `-2.0174` n `228`; crypto_major avg `-1.8606` n `8`; equity avg `-6.6402` n `74`; fx avg `-0.2513` n `6`; index avg `-4.0557` n `23`; metal avg `-4.0636` n `18`; unknown avg `0.7416` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
