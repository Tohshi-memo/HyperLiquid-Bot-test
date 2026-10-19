# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T07:07:24.432103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `13`; crypto_alt avg `0.1331` n `237`; crypto_major avg `0.1163` n `8`; equity avg `0.0373` n `151`; fx avg `-0.006` n `6`; index avg `0.0104` n `26`; metal avg `0.0431` n `20`; unknown avg `-0.0094` n `1192`
- 1h: commodity avg `-0.0249` n `13`; crypto_alt avg `0.0002` n `237`; crypto_major avg `0.1278` n `8`; equity avg `-0.06` n `151`; fx avg `-0.0155` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.523` n `1192`
- 4h: commodity avg `-0.1317` n `13`; crypto_alt avg `0.0886` n `237`; crypto_major avg `0.3207` n `8`; equity avg `0.2936` n `151`; fx avg `-0.033` n `6`; index avg `0.0663` n `26`; metal avg `0.0244` n `20`; unknown avg `1.6316` n `1164`
- 24h: commodity avg `-0.4946` n `13`; crypto_alt avg `0.4107` n `237`; crypto_major avg `1.284` n `8`; equity avg `2.8122` n `151`; fx avg `-0.0384` n `6`; index avg `0.5099` n `26`; metal avg `0.3248` n `20`; unknown avg `2.6483` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1947`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0649`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0631`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
