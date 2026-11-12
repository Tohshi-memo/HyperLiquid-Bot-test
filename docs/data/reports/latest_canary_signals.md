# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T21:52:28.931312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.0311` n `239`; crypto_major avg `-0.1214` n `8`; equity avg `-0.1113` n `162`; fx avg `-0.008` n `6`; index avg `-0.0069` n `27`; metal avg `0.0224` n `20`; unknown avg `11.3872` n `1259`
- 1h: commodity avg `0.0221` n `13`; crypto_alt avg `0.2875` n `239`; crypto_major avg `0.0619` n `8`; equity avg `0.3324` n `162`; fx avg `-0.02` n `6`; index avg `0.0317` n `27`; metal avg `-0.0055` n `20`; unknown avg `185.5033` n `1235`
- 4h: commodity avg `0.4013` n `13`; crypto_alt avg `0.6676` n `239`; crypto_major avg `0.0942` n `8`; equity avg `-0.5316` n `162`; fx avg `0.0242` n `6`; index avg `-0.0516` n `27`; metal avg `-0.0308` n `20`; unknown avg `0.4378` n `1225`
- 24h: commodity avg `0.8754` n `13`; crypto_alt avg `-1.7689` n `239`; crypto_major avg `-2.6562` n `8`; equity avg `-2.3564` n `162`; fx avg `-0.0942` n `6`; index avg `-0.1087` n `27`; metal avg `-0.7177` n `20`; unknown avg `31.3537` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
