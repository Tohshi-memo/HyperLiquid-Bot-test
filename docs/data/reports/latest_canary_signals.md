# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T08:22:31.070493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `0.0031` n `239`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0365` n `168`; fx avg `-0.0005` n `6`; index avg `-0.008` n `27`; metal avg `0.0075` n `20`; unknown avg `12.4716` n `1261`
- 1h: commodity avg `-0.0107` n `13`; crypto_alt avg `-0.154` n `239`; crypto_major avg `0.0565` n `8`; equity avg `-0.0131` n `168`; fx avg `0.0023` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0096` n `20`; unknown avg `13.5009` n `1243`
- 4h: commodity avg `-0.0148` n `13`; crypto_alt avg `-1.5014` n `239`; crypto_major avg `-0.8091` n `8`; equity avg `-0.2253` n `168`; fx avg `-0.0014` n `6`; index avg `-0.0391` n `27`; metal avg `-0.0126` n `20`; unknown avg `9.8283` n `1203`
- 24h: commodity avg `-0.7437` n `13`; crypto_alt avg `-3.2791` n `239`; crypto_major avg `-3.0894` n `8`; equity avg `-0.4369` n `168`; fx avg `-0.0567` n `6`; index avg `0.015` n `27`; metal avg `-0.3384` n `20`; unknown avg `212.4466` n `1001`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
