# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T12:07:30.099136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0546` n `12`; crypto_alt avg `0.0977` n `233`; crypto_major avg `0.0119` n `8`; equity avg `-0.1929` n `136`; fx avg `0.008` n `6`; index avg `-0.0182` n `27`; metal avg `0.0682` n `20`; unknown avg `0.1754` n `892`
- 1h: commodity avg `0.0465` n `12`; crypto_alt avg `0.2066` n `233`; crypto_major avg `0.1626` n `8`; equity avg `-0.3502` n `136`; fx avg `0.0215` n `6`; index avg `-0.0333` n `27`; metal avg `0.0562` n `20`; unknown avg `0.3883` n `892`
- 4h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.216` n `233`; crypto_major avg `-0.0188` n `8`; equity avg `-0.4066` n `136`; fx avg `0.0314` n `6`; index avg `-0.0618` n `27`; metal avg `-0.1534` n `20`; unknown avg `12.9356` n `886`
- 24h: commodity avg `0.5052` n `12`; crypto_alt avg `0.2939` n `233`; crypto_major avg `1.7102` n `8`; equity avg `-1.1077` n `136`; fx avg `0.067` n `6`; index avg `-0.2286` n `27`; metal avg `-0.4012` n `20`; unknown avg `1.0275` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
