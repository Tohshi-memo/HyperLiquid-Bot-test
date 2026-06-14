# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T16:37:32.178138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0602` n `12`; crypto_alt avg `-0.0638` n `228`; crypto_major avg `0.0052` n `8`; equity avg `0.0124` n `74`; fx avg `0.0193` n `6`; index avg `-0.0109` n `23`; metal avg `0.035` n `18`; unknown avg `0.082` n `645`
- 1h: commodity avg `-0.0736` n `12`; crypto_alt avg `0.2645` n `228`; crypto_major avg `0.1338` n `8`; equity avg `0.0083` n `74`; fx avg `0.0071` n `6`; index avg `-0.0039` n `23`; metal avg `0.0109` n `18`; unknown avg `0.0399` n `645`
- 4h: commodity avg `0.107` n `12`; crypto_alt avg `-0.3302` n `228`; crypto_major avg `-0.2484` n `8`; equity avg `-0.133` n `74`; fx avg `-0.0396` n `6`; index avg `0.0792` n `23`; metal avg `-0.1087` n `18`; unknown avg `0.0591` n `645`
- 24h: commodity avg `-0.2243` n `12`; crypto_alt avg `-0.8819` n `228`; crypto_major avg `-0.2235` n `8`; equity avg `0.4717` n `74`; fx avg `-0.0142` n `6`; index avg `0.1444` n `23`; metal avg `-0.1997` n `18`; unknown avg `1.6877` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
