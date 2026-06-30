# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T08:22:31.216568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0662` n `12`; crypto_alt avg `-0.1616` n `228`; crypto_major avg `-0.1967` n `8`; equity avg `-0.0811` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0058` n `23`; metal avg `-0.0868` n `20`; unknown avg `-0.0676` n `765`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `-0.1899` n `228`; crypto_major avg `-0.1104` n `8`; equity avg `-0.0737` n `88`; fx avg `0.0222` n `6`; index avg `-0.0103` n `23`; metal avg `-0.0717` n `20`; unknown avg `0.733` n `765`
- 4h: commodity avg `0.1269` n `12`; crypto_alt avg `-0.2034` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `-0.2188` n `88`; fx avg `0.0721` n `6`; index avg `-0.057` n `23`; metal avg `0.5136` n `20`; unknown avg `-0.7212` n `737`
- 24h: commodity avg `0.0164` n `12`; crypto_alt avg `-0.4526` n `228`; crypto_major avg `0.633` n `8`; equity avg `1.4231` n `88`; fx avg `0.1655` n `6`; index avg `0.1462` n `23`; metal avg `-0.1296` n `20`; unknown avg `9.1803` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
