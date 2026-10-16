# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T09:52:29.116695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0751` n `13`; crypto_alt avg `-0.0144` n `236`; crypto_major avg `0.0027` n `8`; equity avg `-0.0618` n `151`; fx avg `-0.0056` n `6`; index avg `-0.031` n `26`; metal avg `-0.0082` n `20`; unknown avg `1.4145` n `1136`
- 1h: commodity avg `0.0706` n `13`; crypto_alt avg `-0.058` n `236`; crypto_major avg `-0.1585` n `8`; equity avg `-0.0471` n `151`; fx avg `-0.0004` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0383` n `20`; unknown avg `-0.1609` n `1134`
- 4h: commodity avg `0.0209` n `13`; crypto_alt avg `0.2091` n `236`; crypto_major avg `0.1522` n `8`; equity avg `-0.3544` n `151`; fx avg `0.0057` n `6`; index avg `-0.0785` n `26`; metal avg `-0.0053` n `20`; unknown avg `-0.0377` n `1048`
- 24h: commodity avg `0.0355` n `13`; crypto_alt avg `3.9651` n `236`; crypto_major avg `1.8381` n `8`; equity avg `2.577` n `151`; fx avg `0.0055` n `6`; index avg `0.3281` n `26`; metal avg `0.2298` n `20`; unknown avg `27.1224` n `872`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0967`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
