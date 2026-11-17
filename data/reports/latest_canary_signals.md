# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T06:22:25.707457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `13`; crypto_alt avg `-0.1721` n `239`; crypto_major avg `-0.2096` n `8`; equity avg `-0.1418` n `162`; fx avg `-0.0051` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0397` n `20`; unknown avg `-0.0464` n `1264`
- 1h: commodity avg `0.0772` n `13`; crypto_alt avg `-0.4259` n `239`; crypto_major avg `-0.6105` n `8`; equity avg `-0.5963` n `162`; fx avg `0.0289` n `6`; index avg `-0.0483` n `27`; metal avg `-0.1034` n `20`; unknown avg `0.1205` n `1244`
- 4h: commodity avg `0.0054` n `13`; crypto_alt avg `0.4627` n `239`; crypto_major avg `0.451` n `8`; equity avg `-0.3733` n `162`; fx avg `-0.0179` n `6`; index avg `-0.0462` n `27`; metal avg `0.0412` n `20`; unknown avg `-0.2854` n `1224`
- 24h: commodity avg `-1.2235` n `13`; crypto_alt avg `0.8276` n `239`; crypto_major avg `1.3391` n `8`; equity avg `-2.3716` n `162`; fx avg `-0.0146` n `6`; index avg `-0.2278` n `27`; metal avg `-0.0888` n `20`; unknown avg `562.8792` n `981`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
