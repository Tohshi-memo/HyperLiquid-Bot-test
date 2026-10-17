# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T23:52:30.009960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `13`; crypto_alt avg `0.1936` n `236`; crypto_major avg `0.1396` n `8`; equity avg `0.1518` n `151`; fx avg `0.0011` n `6`; index avg `0.007` n `26`; metal avg `0.0185` n `20`; unknown avg `0.0768` n `1193`
- 1h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.0457` n `236`; crypto_major avg `0.0094` n `8`; equity avg `0.3314` n `151`; fx avg `0.0014` n `6`; index avg `0.0268` n `26`; metal avg `0.0182` n `20`; unknown avg `-0.0822` n `1191`
- 4h: commodity avg `-0.0295` n `13`; crypto_alt avg `-1.0035` n `236`; crypto_major avg `-0.6402` n `8`; equity avg `-0.7105` n `151`; fx avg `0.0029` n `6`; index avg `-0.0949` n `26`; metal avg `-0.0464` n `20`; unknown avg `-0.176` n `1171`
- 24h: commodity avg `-0.0692` n `13`; crypto_alt avg `-2.3957` n `236`; crypto_major avg `-1.1569` n `8`; equity avg `-0.5933` n `151`; fx avg `-0.0266` n `6`; index avg `-0.0837` n `26`; metal avg `-0.0694` n `20`; unknown avg `1.3338` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1636`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.135`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
