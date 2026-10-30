# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T14:52:28.776569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `13`; crypto_alt avg `0.6454` n `238`; crypto_major avg `0.653` n `8`; equity avg `0.1983` n `156`; fx avg `0.0054` n `6`; index avg `0.0516` n `27`; metal avg `0.0861` n `20`; unknown avg `1.2709` n `1259`
- 1h: commodity avg `0.0094` n `13`; crypto_alt avg `0.8387` n `238`; crypto_major avg `0.7089` n `8`; equity avg `-0.3102` n `156`; fx avg `0.0292` n `6`; index avg `0.0263` n `27`; metal avg `0.142` n `20`; unknown avg `0.4664` n `1157`
- 4h: commodity avg `-0.0848` n `13`; crypto_alt avg `-0.0853` n `238`; crypto_major avg `-0.7193` n `8`; equity avg `-0.8928` n `156`; fx avg `-0.1285` n `6`; index avg `-0.0009` n `27`; metal avg `-0.1708` n `20`; unknown avg `-0.14` n `1147`
- 24h: commodity avg `0.7113` n `13`; crypto_alt avg `-4.8839` n `238`; crypto_major avg `-3.8866` n `8`; equity avg `-4.901` n `156`; fx avg `-0.0719` n `6`; index avg `-0.3564` n `27`; metal avg `-0.8371` n `20`; unknown avg `37.8321` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
