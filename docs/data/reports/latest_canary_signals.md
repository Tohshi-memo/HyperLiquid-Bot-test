# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T04:37:27.481601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `13`; crypto_alt avg `0.2916` n `236`; crypto_major avg `0.118` n `8`; equity avg `0.0435` n `151`; fx avg `0.0` n `6`; index avg `0.0001` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.2418` n `1193`
- 1h: commodity avg `0.0036` n `13`; crypto_alt avg `0.1015` n `236`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0406` n `151`; fx avg `-0.0025` n `6`; index avg `-0.0021` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.1787` n `1185`
- 4h: commodity avg `0.0546` n `13`; crypto_alt avg `0.3864` n `236`; crypto_major avg `0.0737` n `8`; equity avg `0.1583` n `151`; fx avg `-0.01` n `6`; index avg `0.0126` n `26`; metal avg `0.0194` n `20`; unknown avg `0.0349` n `1183`
- 24h: commodity avg `0.5892` n `13`; crypto_alt avg `-0.919` n `236`; crypto_major avg `-0.895` n `8`; equity avg `-4.2531` n `151`; fx avg `-0.0528` n `6`; index avg `-0.6817` n `26`; metal avg `-0.2599` n `20`; unknown avg `40.6142` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1734`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
