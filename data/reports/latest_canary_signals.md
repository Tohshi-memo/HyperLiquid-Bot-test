# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T13:52:28.397792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `-0.1341` n `239`; crypto_major avg `-0.2281` n `8`; equity avg `-0.069` n `168`; fx avg `0.006` n `6`; index avg `-0.0068` n `27`; metal avg `-0.003` n `20`; unknown avg `19.5541` n `1267`
- 1h: commodity avg `0.0195` n `13`; crypto_alt avg `-0.4331` n `239`; crypto_major avg `-0.4582` n `8`; equity avg `-0.2256` n `168`; fx avg `0.0108` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0429` n `20`; unknown avg `1.2128` n `1255`
- 4h: commodity avg `0.0143` n `13`; crypto_alt avg `-0.819` n `239`; crypto_major avg `-0.7657` n `8`; equity avg `-0.356` n `168`; fx avg `-0.002` n `6`; index avg `-0.0256` n `27`; metal avg `-0.0397` n `20`; unknown avg `302.35` n `1247`
- 24h: commodity avg `-0.179` n `13`; crypto_alt avg `-4.1857` n `239`; crypto_major avg `-3.8107` n `8`; equity avg `-0.3474` n `168`; fx avg `-0.0882` n `6`; index avg `0.0117` n `27`; metal avg `0.0697` n `20`; unknown avg `198.706` n `1094`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
