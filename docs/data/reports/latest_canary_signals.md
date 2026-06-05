# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T01:37:20.570691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5476` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0331` n `12`; crypto_alt avg `0.6863` n `228`; crypto_major avg `0.5467` n `8`; equity avg `0.4373` n `74`; fx avg `0.0071` n `6`; index avg `0.1099` n `23`; metal avg `0.1257` n `18`; unknown avg `0.1898` n `424`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.2498` n `228`; crypto_major avg `-0.156` n `8`; equity avg `-0.0616` n `74`; fx avg `0.0823` n `6`; index avg `-0.0781` n `23`; metal avg `-0.448` n `18`; unknown avg `0.0521` n `424`
- 4h: commodity avg `-0.2884` n `12`; crypto_alt avg `0.087` n `228`; crypto_major avg `0.3607` n `8`; equity avg `-1.1869` n `74`; fx avg `0.1366` n `6`; index avg `-0.837` n `23`; metal avg `-0.8186` n `18`; unknown avg `-0.4854` n `424`
- 24h: commodity avg `-0.225` n `12`; crypto_alt avg `-4.2577` n `228`; crypto_major avg `-2.1864` n `8`; equity avg `-1.3178` n `73`; fx avg `0.2117` n `6`; index avg `-0.5972` n `23`; metal avg `-0.5267` n `18`; unknown avg `0.0312` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
