# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T02:37:26.364579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5464` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `0.1034` n `228`; crypto_major avg `0.1259` n `8`; equity avg `0.0372` n `88`; fx avg `-0.0034` n `6`; index avg `0.009` n `23`; metal avg `0.0464` n `20`; unknown avg `0.1573` n `765`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.9663` n `228`; crypto_major avg `1.0548` n `8`; equity avg `-0.0956` n `88`; fx avg `-0.0245` n `6`; index avg `-0.0574` n `23`; metal avg `0.012` n `20`; unknown avg `2.5076` n `765`
- 4h: commodity avg `-0.0557` n `12`; crypto_alt avg `0.4965` n `228`; crypto_major avg `0.8339` n `8`; equity avg `-0.7125` n `88`; fx avg `0.0712` n `6`; index avg `-0.2571` n `23`; metal avg `-0.4235` n `20`; unknown avg `0.1944` n `765`
- 24h: commodity avg `0.0794` n `12`; crypto_alt avg `-0.9983` n `228`; crypto_major avg `-0.5565` n `8`; equity avg `0.4837` n `88`; fx avg `0.1413` n `6`; index avg `0.0183` n `23`; metal avg `0.1529` n `20`; unknown avg `7.0328` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
