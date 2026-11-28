# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T10:22:27.714559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.0101` n `239`; crypto_major avg `-0.1681` n `8`; equity avg `-0.0114` n `168`; fx avg `0.0043` n `6`; index avg `-0.001` n `27`; metal avg `-0.0042` n `20`; unknown avg `-0.3085` n `1267`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `-0.3259` n `239`; crypto_major avg `-0.248` n `8`; equity avg `0.0629` n `168`; fx avg `-0.0043` n `6`; index avg `0.0119` n `27`; metal avg `0.0196` n `20`; unknown avg `321.181` n `1257`
- 4h: commodity avg `-0.0217` n `13`; crypto_alt avg `-0.2043` n `239`; crypto_major avg `-0.5258` n `8`; equity avg `0.1472` n `168`; fx avg `-0.0078` n `6`; index avg `-0.0027` n `27`; metal avg `0.0532` n `20`; unknown avg `0.4386` n `1209`
- 24h: commodity avg `-0.6642` n `13`; crypto_alt avg `-3.2292` n `239`; crypto_major avg `-3.1975` n `8`; equity avg `-0.3129` n `168`; fx avg `-0.0806` n `6`; index avg `0.0319` n `27`; metal avg `-0.2447` n `20`; unknown avg `190.6744` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
