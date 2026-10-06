# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T00:37:29.453760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `13`; crypto_alt avg `-0.2523` n `235`; crypto_major avg `-0.1438` n `8`; equity avg `0.0436` n `144`; fx avg `-0.0027` n `6`; index avg `0.0076` n `26`; metal avg `-0.0201` n `20`; unknown avg `0.7543` n `1079`
- 1h: commodity avg `0.0441` n `13`; crypto_alt avg `-0.1574` n `235`; crypto_major avg `0.0184` n `8`; equity avg `0.0323` n `144`; fx avg `-0.0178` n `6`; index avg `-0.0021` n `26`; metal avg `0.013` n `20`; unknown avg `0.4679` n `1071`
- 4h: commodity avg `0.0313` n `13`; crypto_alt avg `-0.0132` n `235`; crypto_major avg `0.0792` n `8`; equity avg `0.1439` n `144`; fx avg `-0.0069` n `6`; index avg `0.0094` n `26`; metal avg `0.004` n `20`; unknown avg `-0.1653` n `1019`
- 24h: commodity avg `-0.1147` n `13`; crypto_alt avg `0.0822` n `235`; crypto_major avg `0.2473` n `8`; equity avg `0.1739` n `144`; fx avg `-0.0945` n `6`; index avg `0.1121` n `26`; metal avg `-0.0042` n `20`; unknown avg `625.4948` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
