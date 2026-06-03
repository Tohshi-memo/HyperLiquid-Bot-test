# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T03:37:25.348872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.6185` n `228`; crypto_major avg `-0.5469` n `8`; equity avg `0.0725` n `72`; fx avg `0.0006` n `6`; index avg `0.014` n `23`; metal avg `-0.0276` n `18`; unknown avg `-0.294` n `420`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `-0.6249` n `228`; crypto_major avg `-0.8428` n `8`; equity avg `0.0467` n `72`; fx avg `0.0164` n `6`; index avg `-0.0275` n `23`; metal avg `0.2288` n `18`; unknown avg `-0.4748` n `420`
- 4h: commodity avg `-0.3596` n `12`; crypto_alt avg `0.8729` n `228`; crypto_major avg `-0.2677` n `8`; equity avg `0.2138` n `72`; fx avg `0.0642` n `6`; index avg `0.3783` n `23`; metal avg `0.458` n `18`; unknown avg `-0.3889` n `419`
- 24h: commodity avg `0.7004` n `12`; crypto_alt avg `-5.0117` n `228`; crypto_major avg `-6.8579` n `8`; equity avg `1.3381` n `72`; fx avg `0.0415` n `6`; index avg `1.5811` n `23`; metal avg `0.0448` n `18`; unknown avg `-0.6424` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
