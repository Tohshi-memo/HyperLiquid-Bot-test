# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T19:37:34.180766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-4.883` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1478` n `12`; crypto_alt avg `0.0231` n `228`; crypto_major avg `0.0215` n `8`; equity avg `0.0419` n `77`; fx avg `0.0001` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0751` n `18`; unknown avg `-0.0194` n `687`
- 1h: commodity avg `0.2786` n `12`; crypto_alt avg `-0.9052` n `228`; crypto_major avg `-0.5367` n `8`; equity avg `-0.1483` n `77`; fx avg `-0.0284` n `6`; index avg `-0.0315` n `23`; metal avg `-0.0747` n `18`; unknown avg `0.132` n `687`
- 4h: commodity avg `0.5734` n `12`; crypto_alt avg `-1.0707` n `228`; crypto_major avg `0.0041` n `8`; equity avg `4.8871` n `77`; fx avg `-0.0233` n `6`; index avg `0.0353` n `23`; metal avg `-0.6912` n `18`; unknown avg `3.2095` n `687`
- 24h: commodity avg `-0.4572` n `12`; crypto_alt avg `4.5489` n `228`; crypto_major avg `6.6829` n `8`; equity avg `2.8659` n `76`; fx avg `0.0306` n `6`; index avg `1.2663` n `23`; metal avg `2.1631` n `18`; unknown avg `5.3264` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
