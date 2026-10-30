# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T12:07:26.311457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `-0.0196` n `238`; crypto_major avg `-0.0767` n `8`; equity avg `0.1057` n `156`; fx avg `0.0071` n `6`; index avg `0.011` n `27`; metal avg `0.0399` n `20`; unknown avg `0.4756` n `1249`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `-0.2914` n `238`; crypto_major avg `-0.5182` n `8`; equity avg `-0.1394` n `156`; fx avg `-0.0115` n `6`; index avg `-0.0216` n `27`; metal avg `-0.1356` n `20`; unknown avg `0.1197` n `1249`
- 4h: commodity avg `0.0369` n `13`; crypto_alt avg `0.6849` n `238`; crypto_major avg `-0.1282` n `8`; equity avg `-0.7064` n `156`; fx avg `-0.0252` n `6`; index avg `-0.1155` n `27`; metal avg `-0.1046` n `20`; unknown avg `37.2801` n `1236`
- 24h: commodity avg `0.1983` n `13`; crypto_alt avg `-3.5831` n `238`; crypto_major avg `-2.3112` n `8`; equity avg `-3.7673` n `156`; fx avg `0.0605` n `6`; index avg `-0.3981` n `27`; metal avg `-0.6724` n `20`; unknown avg `23.1674` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
