# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T12:52:28.877078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `13`; crypto_alt avg `-0.5353` n `236`; crypto_major avg `-0.3736` n `8`; equity avg `-0.1408` n `151`; fx avg `-0.0053` n `6`; index avg `-0.0192` n `26`; metal avg `-0.025` n `20`; unknown avg `-0.0353` n `1136`
- 1h: commodity avg `-0.2912` n `13`; crypto_alt avg `-0.5185` n `236`; crypto_major avg `-0.6797` n `8`; equity avg `-0.0849` n `151`; fx avg `-0.03` n `6`; index avg `0.0141` n `26`; metal avg `-0.0506` n `20`; unknown avg `0.3273` n `1128`
- 4h: commodity avg `-0.0424` n `13`; crypto_alt avg `-0.2819` n `236`; crypto_major avg `-0.4626` n `8`; equity avg `-0.781` n `151`; fx avg `0.0032` n `6`; index avg `-0.0575` n `26`; metal avg `-0.0826` n `20`; unknown avg `3.8819` n `1128`
- 24h: commodity avg `-0.0255` n `13`; crypto_alt avg `4.5369` n `236`; crypto_major avg `2.352` n `8`; equity avg `2.2968` n `151`; fx avg `0.0023` n `6`; index avg `0.2852` n `26`; metal avg `0.2605` n `20`; unknown avg `24.9369` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.082`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
