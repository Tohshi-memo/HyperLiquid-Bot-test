# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T07:37:25.400752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `-0.1667` n `239`; crypto_major avg `-0.0888` n `8`; equity avg `-0.053` n `166`; fx avg `-0.0193` n `6`; index avg `-0.0104` n `27`; metal avg `0.0107` n `20`; unknown avg `315.7739` n `1266`
- 1h: commodity avg `0.1819` n `13`; crypto_alt avg `-0.2706` n `239`; crypto_major avg `-0.1099` n `8`; equity avg `-0.1392` n `166`; fx avg `-0.0281` n `6`; index avg `-0.0195` n `27`; metal avg `0.1095` n `20`; unknown avg `13.3841` n `1254`
- 4h: commodity avg `0.1166` n `13`; crypto_alt avg `0.8801` n `239`; crypto_major avg `0.3439` n `8`; equity avg `-0.2735` n `166`; fx avg `0.0181` n `6`; index avg `-0.0201` n `27`; metal avg `-0.1481` n `20`; unknown avg `-0.1207` n `1206`
- 24h: commodity avg `-0.8546` n `13`; crypto_alt avg `0.3182` n `239`; crypto_major avg `-0.1462` n `8`; equity avg `3.9562` n `166`; fx avg `-0.2502` n `6`; index avg `0.6143` n `27`; metal avg `-0.2898` n `20`; unknown avg `687.6734` n `1034`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
