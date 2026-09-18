# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T19:37:26.568876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0821` n `234`; crypto_major avg `-0.002` n `8`; equity avg `-0.048` n `140`; fx avg `0.0076` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0081` n `20`; unknown avg `913.9437` n `938`
- 1h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.464` n `234`; crypto_major avg `0.3325` n `8`; equity avg `0.2958` n `140`; fx avg `0.0115` n `6`; index avg `0.0455` n `26`; metal avg `-0.0567` n `20`; unknown avg `115.58` n `936`
- 4h: commodity avg `-0.2996` n `12`; crypto_alt avg `1.0785` n `234`; crypto_major avg `1.0442` n `8`; equity avg `0.5094` n `140`; fx avg `0.0085` n `6`; index avg `0.0882` n `26`; metal avg `0.1131` n `20`; unknown avg `15.8365` n `906`
- 24h: commodity avg `-0.0523` n `12`; crypto_alt avg `6.7694` n `234`; crypto_major avg `7.2502` n `8`; equity avg `1.0251` n `140`; fx avg `0.1997` n `6`; index avg `-0.0395` n `26`; metal avg `0.3872` n `20`; unknown avg `10.6463` n `715`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
