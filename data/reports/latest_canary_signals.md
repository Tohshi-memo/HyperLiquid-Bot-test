# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T23:22:51.215240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.88` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `3.8352` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7785` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `0.1322` n `228`; crypto_major avg `0.1228` n `8`; equity avg `-0.0342` n `74`; fx avg `0.0052` n `6`; index avg `-0.0231` n `23`; metal avg `-0.1644` n `18`; unknown avg `-0.1729` n `645`
- 1h: commodity avg `-0.0574` n `12`; crypto_alt avg `0.0822` n `228`; crypto_major avg `0.083` n `8`; equity avg `-0.1774` n `74`; fx avg `-0.0006` n `6`; index avg `-0.1555` n `23`; metal avg `-0.3297` n `18`; unknown avg `6.6042` n `645`
- 4h: commodity avg `-0.9812` n `12`; crypto_alt avg `2.7394` n `228`; crypto_major avg `2.854` n `8`; equity avg `1.0755` n `74`; fx avg `0.1325` n `6`; index avg `0.1912` n `23`; metal avg `1.4634` n `18`; unknown avg `2.9691` n `645`
- 24h: commodity avg `-0.9092` n `12`; crypto_alt avg `1.2566` n `228`; crypto_major avg `1.7607` n `8`; equity avg `1.2279` n `74`; fx avg `0.1044` n `6`; index avg `0.3453` n `23`; metal avg `1.3486` n `18`; unknown avg `0.7577` n `593`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
