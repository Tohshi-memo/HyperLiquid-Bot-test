# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T14:56:39.390757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.1242` n `238`; crypto_major avg `0.0526` n `8`; equity avg `0.0728` n `156`; fx avg `0.0077` n `6`; index avg `0.0092` n `27`; metal avg `0.0072` n `20`; unknown avg `-0.0067` n `1258`
- 1h: commodity avg `-0.0509` n `13`; crypto_alt avg `0.0741` n `238`; crypto_major avg `-0.1279` n `8`; equity avg `0.1299` n `156`; fx avg `0.003` n `6`; index avg `0.0165` n `27`; metal avg `0.0107` n `20`; unknown avg `1.4966` n `1254`
- 4h: commodity avg `-0.1139` n `13`; crypto_alt avg `0.4584` n `238`; crypto_major avg `0.0479` n `8`; equity avg `0.0756` n `156`; fx avg `-0.0042` n `6`; index avg `0.0023` n `27`; metal avg `0.0085` n `20`; unknown avg `-0.1475` n `1222`
- 24h: commodity avg `-0.3228` n `13`; crypto_alt avg `0.7495` n `238`; crypto_major avg `-0.3069` n `8`; equity avg `-0.5832` n `156`; fx avg `0.0245` n `6`; index avg `-0.1403` n `27`; metal avg `-0.1568` n `20`; unknown avg `271.6048` n `1099`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
