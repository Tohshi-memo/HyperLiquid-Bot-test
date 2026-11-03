# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T00:22:28.956445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `13`; crypto_alt avg `0.2953` n `239`; crypto_major avg `0.3203` n `8`; equity avg `0.1248` n `157`; fx avg `-0.0168` n `6`; index avg `0.0095` n `27`; metal avg `0.0501` n `20`; unknown avg `0.6434` n `1264`
- 1h: commodity avg `-0.0173` n `13`; crypto_alt avg `0.3468` n `239`; crypto_major avg `0.3219` n `8`; equity avg `-0.1397` n `157`; fx avg `-0.027` n `6`; index avg `-0.0331` n `27`; metal avg `0.0746` n `20`; unknown avg `4.8638` n `1252`
- 4h: commodity avg `-0.0355` n `13`; crypto_alt avg `0.4183` n `239`; crypto_major avg `0.4033` n `8`; equity avg `-0.0462` n `157`; fx avg `-0.0433` n `6`; index avg `-0.0237` n `27`; metal avg `0.0819` n `20`; unknown avg `232.2243` n `1162`
- 24h: commodity avg `-1.4779` n `13`; crypto_alt avg `-2.049` n `238`; crypto_major avg `-1.0137` n `8`; equity avg `-2.8222` n `157`; fx avg `0.1701` n `6`; index avg `-0.0725` n `27`; metal avg `0.175` n `20`; unknown avg `15.2816` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
