# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T22:37:25.523479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2747` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2181` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8105` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.222` n `12`; crypto_alt avg `-0.2885` n `228`; crypto_major avg `-0.0043` n `8`; equity avg `-0.1174` n `74`; fx avg `-0.0026` n `6`; index avg `0.0565` n `23`; metal avg `-0.0396` n `18`; unknown avg `-0.207` n `425`
- 1h: commodity avg `0.2195` n `12`; crypto_alt avg `-0.782` n `228`; crypto_major avg `-0.6196` n `8`; equity avg `-0.1262` n `74`; fx avg `-0.0046` n `6`; index avg `0.0429` n `23`; metal avg `-0.0273` n `18`; unknown avg `-0.27` n `425`
- 4h: commodity avg `-0.1733` n `12`; crypto_alt avg `2.0339` n `228`; crypto_major avg `2.1014` n `8`; equity avg `0.2909` n `74`; fx avg `0.0002` n `6`; index avg `-0.5339` n `23`; metal avg `-0.1167` n `18`; unknown avg `1.9489` n `424`
- 24h: commodity avg `-1.5565` n `12`; crypto_alt avg `-5.2564` n `228`; crypto_major avg `-4.5692` n `8`; equity avg `-5.8321` n `74`; fx avg `-0.0447` n `6`; index avg `-4.1026` n `23`; metal avg `-4.526` n `18`; unknown avg `-1.3598` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
