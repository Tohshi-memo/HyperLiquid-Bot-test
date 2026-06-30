# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T07:52:30.398919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0437` n `12`; crypto_alt avg `-0.0316` n `228`; crypto_major avg `0.0111` n `8`; equity avg `-0.0953` n `88`; fx avg `0.0301` n `6`; index avg `-0.0376` n `23`; metal avg `-0.0215` n `20`; unknown avg `-0.0142` n `765`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.2781` n `228`; crypto_major avg `-0.0837` n `8`; equity avg `-0.0254` n `88`; fx avg `0.0467` n `6`; index avg `-0.0106` n `23`; metal avg `-0.0347` n `20`; unknown avg `0.106` n `765`
- 4h: commodity avg `0.0991` n `12`; crypto_alt avg `-0.2371` n `228`; crypto_major avg `-0.1519` n `8`; equity avg `-0.0006` n `88`; fx avg `0.0744` n `6`; index avg `-0.0092` n `23`; metal avg `0.6847` n `20`; unknown avg `7.0698` n `737`
- 24h: commodity avg `0.06` n `12`; crypto_alt avg `-0.5941` n `228`; crypto_major avg `0.5701` n `8`; equity avg `1.6237` n `88`; fx avg `0.1822` n `6`; index avg `0.1268` n `23`; metal avg `-0.1115` n `20`; unknown avg `9.412` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
