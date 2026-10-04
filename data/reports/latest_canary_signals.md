# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T01:07:51.409283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `13`; crypto_alt avg `-0.0597` n `235`; crypto_major avg `0.0075` n `8`; equity avg `0.0029` n `143`; fx avg `-0.0015` n `6`; index avg `-0.0011` n `26`; metal avg `0.0005` n `20`; unknown avg `0.0382` n `1077`
- 1h: commodity avg `0.0019` n `13`; crypto_alt avg `-0.1248` n `235`; crypto_major avg `0.0499` n `8`; equity avg `-0.0052` n `143`; fx avg `-0.0014` n `6`; index avg `-0.0037` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.0457` n `1077`
- 4h: commodity avg `-0.0632` n `13`; crypto_alt avg `0.1939` n `235`; crypto_major avg `0.1275` n `8`; equity avg `0.0668` n `143`; fx avg `-0.0008` n `6`; index avg `0.0034` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.2122` n `1055`
- 24h: commodity avg `0.0053` n `13`; crypto_alt avg `1.2242` n `235`; crypto_major avg `0.4323` n `8`; equity avg `0.1748` n `143`; fx avg `-0.03` n `6`; index avg `0.0323` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.0441` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
