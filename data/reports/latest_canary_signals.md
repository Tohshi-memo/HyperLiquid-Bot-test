# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T08:40:12.256811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0515` n `13`; crypto_alt avg `-0.1418` n `236`; crypto_major avg `-0.0897` n `8`; equity avg `-0.022` n `151`; fx avg `-0.0188` n `6`; index avg `0.0126` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.0092` n `1193`
- 1h: commodity avg `0.0549` n `13`; crypto_alt avg `-0.1829` n `236`; crypto_major avg `-0.1532` n `8`; equity avg `-0.0488` n `151`; fx avg `-0.0161` n `6`; index avg `0.0088` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.0697` n `1175`
- 4h: commodity avg `-0.1835` n `13`; crypto_alt avg `-0.7184` n `236`; crypto_major avg `0.0219` n `8`; equity avg `0.0217` n `151`; fx avg `-0.0128` n `6`; index avg `0.0435` n `26`; metal avg `-0.0078` n `20`; unknown avg `-0.0099` n `1157`
- 24h: commodity avg `0.4737` n `13`; crypto_alt avg `-2.2584` n `236`; crypto_major avg `-1.4354` n `8`; equity avg `-3.8773` n `151`; fx avg `0.0353` n `6`; index avg `-0.5748` n `26`; metal avg `-0.252` n `20`; unknown avg `8.6647` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1818`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1439`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
