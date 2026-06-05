# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T20:31:23.949088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.6415` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.5444` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.2589` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7948` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.5525` n `228`; crypto_major avg `0.4416` n `8`; equity avg `0.1173` n `74`; fx avg `0.0054` n `6`; index avg `-0.0199` n `23`; metal avg `0.1106` n `18`; unknown avg `0.1431` n `425`
- 1h: commodity avg `0.036` n `12`; crypto_alt avg `2.6092` n `228`; crypto_major avg `2.2949` n `8`; equity avg `-0.3466` n `74`; fx avg `-0.001` n `6`; index avg `-0.4581` n `23`; metal avg `-0.2495` n `18`; unknown avg `2.3984` n `425`
- 4h: commodity avg `0.1256` n `12`; crypto_alt avg `0.7518` n `228`; crypto_major avg `0.5658` n `8`; equity avg `-1.229` n `74`; fx avg `-0.0495` n `6`; index avg `-1.5846` n `23`; metal avg `-0.6544` n `18`; unknown avg `0.9474` n `424`
- 24h: commodity avg `-1.6286` n `12`; crypto_alt avg `-7.5002` n `228`; crypto_major avg `-6.1735` n `8`; equity avg `-6.4567` n `74`; fx avg `-0.0505` n `6`; index avg `-4.5568` n `23`; metal avg `-4.6669` n `18`; unknown avg `-1.161` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
