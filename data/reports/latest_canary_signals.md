# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T12:22:29.595214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.1748` n `239`; crypto_major avg `-0.2588` n `8`; equity avg `-0.0449` n `162`; fx avg `0.0083` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0089` n `20`; unknown avg `2.3096` n `1260`
- 1h: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.0877` n `239`; crypto_major avg `-0.256` n `8`; equity avg `-0.0365` n `162`; fx avg `0.023` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.2264` n `1252`
- 4h: commodity avg `-0.056` n `13`; crypto_alt avg `-0.3875` n `239`; crypto_major avg `-0.1047` n `8`; equity avg `0.0077` n `162`; fx avg `0.0101` n `6`; index avg `-0.0054` n `27`; metal avg `0.0171` n `20`; unknown avg `85.1389` n `1178`
- 24h: commodity avg `-0.2488` n `13`; crypto_alt avg `-3.5419` n `239`; crypto_major avg `-3.8338` n `8`; equity avg `-3.1103` n `162`; fx avg `-0.1209` n `6`; index avg `-0.2699` n `27`; metal avg `-0.4169` n `20`; unknown avg `2.4402` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
