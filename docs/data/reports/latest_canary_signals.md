# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T00:37:32.237683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `0.0166` n `233`; crypto_major avg `0.0494` n `8`; equity avg `-0.1086` n `134`; fx avg `-0.0025` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0209` n `20`; unknown avg `0.1505` n `791`
- 1h: commodity avg `-0.1009` n `12`; crypto_alt avg `-0.3247` n `233`; crypto_major avg `-0.0646` n `8`; equity avg `-0.0636` n `134`; fx avg `0.0002` n `6`; index avg `0.0196` n `26`; metal avg `-0.0165` n `20`; unknown avg `0.0455` n `789`
- 4h: commodity avg `-0.0081` n `12`; crypto_alt avg `-1.8699` n `233`; crypto_major avg `-0.8868` n `8`; equity avg `-0.3103` n `134`; fx avg `-0.014` n `6`; index avg `0.0011` n `26`; metal avg `-0.0161` n `20`; unknown avg `3.9036` n `715`
- 24h: commodity avg `0.0306` n `12`; crypto_alt avg `-3.1821` n `233`; crypto_major avg `-2.1916` n `8`; equity avg `-0.6637` n `134`; fx avg `-0.022` n `6`; index avg `-0.1432` n `26`; metal avg `0.5072` n `20`; unknown avg `1.1663` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
