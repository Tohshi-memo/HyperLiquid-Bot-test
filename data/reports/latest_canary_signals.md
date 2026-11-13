# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T16:07:31.113779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6415` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0827` n `13`; crypto_alt avg `0.2791` n `239`; crypto_major avg `0.1893` n `8`; equity avg `-0.2281` n `162`; fx avg `-0.0015` n `6`; index avg `-0.0208` n `27`; metal avg `-0.0252` n `20`; unknown avg `0.8236` n `1250`
- 1h: commodity avg `-0.0911` n `13`; crypto_alt avg `-0.3679` n `239`; crypto_major avg `-0.6317` n `8`; equity avg `-0.87` n `162`; fx avg `-0.046` n `6`; index avg `-0.0885` n `27`; metal avg `-0.1731` n `20`; unknown avg `0.3789` n `1250`
- 4h: commodity avg `-0.1002` n `13`; crypto_alt avg `-0.0866` n `239`; crypto_major avg `-0.7857` n `8`; equity avg `-3.4272` n `162`; fx avg `-0.0453` n `6`; index avg `-0.3329` n `27`; metal avg `-0.2716` n `20`; unknown avg `5.3261` n `1246`
- 24h: commodity avg `0.5213` n `13`; crypto_alt avg `0.1126` n `239`; crypto_major avg `-1.8888` n `8`; equity avg `-4.2875` n `162`; fx avg `-0.0355` n `6`; index avg `-0.3976` n `27`; metal avg `-0.2016` n `20`; unknown avg `2.2036` n `1073`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
