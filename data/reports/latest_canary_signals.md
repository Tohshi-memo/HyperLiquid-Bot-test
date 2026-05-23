# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T21:22:17.477748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.0122` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.648` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6409` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.5177` n `12`; crypto_alt avg `-0.054` n `228`; crypto_major avg `-0.0766` n `8`; equity avg `0.1896` n `67`; fx avg `0.0095` n `6`; index avg `0.2177` n `23`; metal avg `-0.1126` n `18`; unknown avg `-0.0991` n `396`
- 1h: commodity avg `-1.3392` n `12`; crypto_alt avg `1.5791` n `228`; crypto_major avg `1.3088` n `8`; equity avg `0.732` n `67`; fx avg `0.0492` n `6`; index avg `0.3548` n `23`; metal avg `0.5031` n `18`; unknown avg `0.4319` n `396`
- 4h: commodity avg `-2.7052` n `12`; crypto_alt avg `2.4807` n `228`; crypto_major avg `2.307` n `8`; equity avg `1.4178` n `67`; fx avg `0.0376` n `6`; index avg `0.7801` n `23`; metal avg `0.6661` n `18`; unknown avg `3.4587` n `396`
- 24h: commodity avg `-2.8024` n `12`; crypto_alt avg `2.0667` n `228`; crypto_major avg `1.9099` n `8`; equity avg `1.4024` n `67`; fx avg `0.0171` n `6`; index avg `0.8127` n `23`; metal avg `0.7627` n `18`; unknown avg `-0.1869` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
