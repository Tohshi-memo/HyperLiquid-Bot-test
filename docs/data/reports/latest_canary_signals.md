# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:08:56.873825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2823` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1624` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7675` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `0.0321` n `230`; crypto_major avg `0.0674` n `8`; equity avg `0.0961` n `121`; fx avg `0.0043` n `6`; index avg `0.0048` n `25`; metal avg `0.0581` n `20`; unknown avg `0.0011` n `792`
- 1h: commodity avg `-0.2068` n `12`; crypto_alt avg `0.2405` n `230`; crypto_major avg `0.4856` n `8`; equity avg `0.0812` n `121`; fx avg `0.0103` n `6`; index avg `0.0268` n `25`; metal avg `0.1332` n `20`; unknown avg `1.047` n `792`
- 4h: commodity avg `-0.2996` n `12`; crypto_alt avg `0.8576` n `230`; crypto_major avg `1.9827` n `8`; equity avg `-0.1797` n `121`; fx avg `0.003` n `6`; index avg `-0.0797` n `25`; metal avg `0.2152` n `20`; unknown avg `0.1289` n `792`
- 24h: commodity avg `-0.0222` n `12`; crypto_alt avg `2.8422` n `230`; crypto_major avg `4.9826` n `8`; equity avg `-0.3767` n `120`; fx avg `-0.1957` n `6`; index avg `-0.0071` n `25`; metal avg `0.9581` n `20`; unknown avg `0.3869` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
