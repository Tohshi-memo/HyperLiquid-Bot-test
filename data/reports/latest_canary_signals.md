# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T10:22:26.712849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `0.1214` n `235`; crypto_major avg `0.0098` n `8`; equity avg `0.0112` n `143`; fx avg `0.0007` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.0088` n `984`
- 1h: commodity avg `0.0397` n `13`; crypto_alt avg `0.5663` n `235`; crypto_major avg `0.0294` n `8`; equity avg `0.0248` n `143`; fx avg `-0.0024` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0094` n `20`; unknown avg `-0.1352` n `982`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `0.1356` n `235`; crypto_major avg `-0.0455` n `8`; equity avg `0.0609` n `143`; fx avg `-0.0118` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0144` n `20`; unknown avg `2.0917` n `966`
- 24h: commodity avg `0.6763` n `13`; crypto_alt avg `-1.7807` n `235`; crypto_major avg `-2.2801` n `8`; equity avg `0.1594` n `142`; fx avg `0.0216` n `6`; index avg `0.1503` n `26`; metal avg `-0.1714` n `20`; unknown avg `-0.3587` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
