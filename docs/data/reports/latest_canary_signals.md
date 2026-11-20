# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T00:37:31.351588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0612` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0168` n `13`; crypto_alt avg `-0.2989` n `239`; crypto_major avg `-0.4206` n `8`; equity avg `-0.5472` n `165`; fx avg `0.0006` n `6`; index avg `-0.1283` n `27`; metal avg `-0.1156` n `20`; unknown avg `-0.2722` n `1262`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.0076` n `239`; crypto_major avg `0.1417` n `8`; equity avg `-0.0781` n `165`; fx avg `0.0347` n `6`; index avg `-0.0393` n `27`; metal avg `0.0591` n `20`; unknown avg `-0.0284` n `1254`
- 4h: commodity avg `-0.013` n `13`; crypto_alt avg `-0.1518` n `239`; crypto_major avg `-0.2663` n `8`; equity avg `-2.3275` n `165`; fx avg `0.0129` n `6`; index avg `-0.1631` n `27`; metal avg `-0.5028` n `20`; unknown avg `3.4745` n `1230`
- 24h: commodity avg `0.0453` n `13`; crypto_alt avg `-1.2894` n `239`; crypto_major avg `-0.9664` n `8`; equity avg `-5.0645` n `165`; fx avg `0.0526` n `6`; index avg `-0.416` n `27`; metal avg `-1.2406` n `20`; unknown avg `7.9554` n `1170`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
