# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T08:37:27.466495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.076` n `12`; crypto_alt avg `-0.3207` n `228`; crypto_major avg `-0.2704` n `8`; equity avg `-0.1144` n `88`; fx avg `-0.0121` n `6`; index avg `-0.0351` n `23`; metal avg `-0.0607` n `20`; unknown avg `-0.0744` n `765`
- 1h: commodity avg `0.1675` n `12`; crypto_alt avg `-0.4558` n `228`; crypto_major avg `-0.4373` n `8`; equity avg `-0.2437` n `88`; fx avg `0.0028` n `6`; index avg `-0.0558` n `23`; metal avg `-0.1457` n `20`; unknown avg `-0.1227` n `765`
- 4h: commodity avg `0.2298` n `12`; crypto_alt avg `-0.7252` n `228`; crypto_major avg `-0.6816` n `8`; equity avg `-0.4446` n `88`; fx avg `0.0632` n `6`; index avg `-0.1439` n `23`; metal avg `0.2342` n `20`; unknown avg `-0.8497` n `737`
- 24h: commodity avg `0.1031` n `12`; crypto_alt avg `-0.732` n `228`; crypto_major avg `0.4` n `8`; equity avg `1.3189` n `88`; fx avg `0.1528` n `6`; index avg `0.1078` n `23`; metal avg `-0.2075` n `20`; unknown avg `8.7066` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
