# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T07:37:23.190115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.9146` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9352` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1074` n `12`; crypto_alt avg `0.1075` n `228`; crypto_major avg `0.0718` n `8`; equity avg `-0.1072` n `72`; fx avg `-0.0047` n `6`; index avg `-0.0268` n `23`; metal avg `-0.1049` n `18`; unknown avg `-0.148` n `420`
- 1h: commodity avg `0.3199` n `12`; crypto_alt avg `0.0797` n `228`; crypto_major avg `-0.1032` n `8`; equity avg `-0.1264` n `72`; fx avg `0.0009` n `6`; index avg `-0.0004` n `23`; metal avg `-0.1159` n `18`; unknown avg `-0.0163` n `420`
- 4h: commodity avg `0.4968` n `12`; crypto_alt avg `3.0483` n `228`; crypto_major avg `2.2012` n `8`; equity avg `0.266` n `72`; fx avg `0.0714` n `6`; index avg `-0.0361` n `23`; metal avg `-0.7134` n `18`; unknown avg `0.4753` n `410`
- 24h: commodity avg `1.2048` n `12`; crypto_alt avg `-1.1077` n `228`; crypto_major avg `-3.5527` n `8`; equity avg `0.8175` n `72`; fx avg `0.0422` n `6`; index avg `0.9946` n `23`; metal avg `-1.7505` n `18`; unknown avg `-0.025` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
