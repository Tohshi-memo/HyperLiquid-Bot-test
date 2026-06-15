# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T16:37:39.901002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-4.1819` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.2573` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1713` n `12`; crypto_alt avg `-0.1575` n `228`; crypto_major avg `0.336` n `8`; equity avg `0.0263` n `77`; fx avg `0.0119` n `6`; index avg `-0.0266` n `23`; metal avg `-0.2738` n `18`; unknown avg `-0.0515` n `687`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `0.5344` n `228`; crypto_major avg `0.9293` n `8`; equity avg `5.1112` n `77`; fx avg `0.0168` n `6`; index avg `0.1835` n `23`; metal avg `-0.4169` n `18`; unknown avg `0.0047` n `687`
- 4h: commodity avg `0.3771` n `12`; crypto_alt avg `0.9855` n `228`; crypto_major avg `1.9001` n `8`; equity avg `1.4742` n `76`; fx avg `0.0204` n `6`; index avg `0.533` n `23`; metal avg `-0.3572` n `18`; unknown avg `0.5064` n `687`
- 24h: commodity avg `-0.825` n `12`; crypto_alt avg `6.2536` n `228`; crypto_major avg `7.5415` n `8`; equity avg `3.0459` n `76`; fx avg `0.0675` n `6`; index avg `1.3537` n `23`; metal avg `2.3798` n `18`; unknown avg `2.7099` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.15`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0969`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0631`, n `669`, weak_sample_signal
