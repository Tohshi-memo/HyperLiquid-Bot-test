# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T16:31:48.197982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-4.0372` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `3.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.4791` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.5651` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1139` n `12`; crypto_alt avg `0.016` n `228`; crypto_major avg `0.585` n `8`; equity avg `0.1322` n `77`; fx avg `0.0117` n `6`; index avg `0.0076` n `23`; metal avg `-0.2421` n `18`; unknown avg `-0.064` n `687`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `0.7095` n `228`; crypto_major avg `1.1797` n `8`; equity avg `5.2169` n `77`; fx avg `0.0165` n `6`; index avg `0.2179` n `23`; metal avg `-0.3854` n `18`; unknown avg `-0.0059` n `687`
- 4h: commodity avg `0.32` n `12`; crypto_alt avg `1.1639` n `228`; crypto_major avg `2.1536` n `8`; equity avg `1.5838` n `76`; fx avg `0.0202` n `6`; index avg `0.5677` n `23`; metal avg `-0.3255` n `18`; unknown avg `0.4966` n `687`
- 24h: commodity avg `-0.8807` n `12`; crypto_alt avg `6.4456` n `228`; crypto_major avg `7.8144` n `8`; equity avg `3.1582` n `76`; fx avg `0.0673` n `6`; index avg `1.3892` n `23`; metal avg `2.4128` n `18`; unknown avg `2.7301` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1531`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.153`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1118`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.098`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0966`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0933`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `669`, weak_sample_signal
