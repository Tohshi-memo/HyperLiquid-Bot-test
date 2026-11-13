# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T16:52:32.148542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6451` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1005` n `13`; crypto_alt avg `-0.3158` n `239`; crypto_major avg `-0.1086` n `8`; equity avg `-0.0637` n `162`; fx avg `-0.0043` n `6`; index avg `-0.0266` n `27`; metal avg `-0.0754` n `20`; unknown avg `1.6443` n `1262`
- 1h: commodity avg `-0.1684` n `13`; crypto_alt avg `-0.1362` n `239`; crypto_major avg `-0.2205` n `8`; equity avg `-0.1225` n `162`; fx avg `-0.01` n `6`; index avg `-0.0331` n `27`; metal avg `-0.0908` n `20`; unknown avg `22.5384` n `1254`
- 4h: commodity avg `-0.3905` n `13`; crypto_alt avg `-0.4836` n `239`; crypto_major avg `-1.0804` n `8`; equity avg `-2.7255` n `162`; fx avg `-0.0468` n `6`; index avg `-0.2928` n `27`; metal avg `-0.291` n `20`; unknown avg `1.2429` n `1248`
- 24h: commodity avg `0.0841` n `13`; crypto_alt avg `0.1231` n `239`; crypto_major avg `-1.8427` n `8`; equity avg `-3.8973` n `162`; fx avg `-0.0159` n `6`; index avg `-0.3738` n `27`; metal avg `-0.3087` n `20`; unknown avg `1.8746` n `1089`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
