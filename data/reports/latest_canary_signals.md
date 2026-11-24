# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T14:07:30.160950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1151` n `13`; crypto_alt avg `0.0739` n `239`; crypto_major avg `0.0882` n `8`; equity avg `0.0469` n `166`; fx avg `0.0033` n `6`; index avg `0.0101` n `27`; metal avg `-0.0197` n `20`; unknown avg `159.8774` n `1249`
- 1h: commodity avg `0.2578` n `13`; crypto_alt avg `-0.1409` n `239`; crypto_major avg `-0.3748` n `8`; equity avg `-0.1634` n `166`; fx avg `-0.0061` n `6`; index avg `-0.0252` n `27`; metal avg `-0.1047` n `20`; unknown avg `160.1811` n `1251`
- 4h: commodity avg `0.2759` n `13`; crypto_alt avg `-0.8644` n `239`; crypto_major avg `-0.329` n `8`; equity avg `-0.5535` n `166`; fx avg `0.0542` n `6`; index avg `-0.1151` n `27`; metal avg `0.0444` n `20`; unknown avg `163.4318` n `1222`
- 24h: commodity avg `-0.0808` n `13`; crypto_alt avg `-3.994` n `239`; crypto_major avg `-4.7768` n `8`; equity avg `-3.2301` n `166`; fx avg `0.0981` n `6`; index avg `-0.2648` n `27`; metal avg `-0.8473` n `20`; unknown avg `6.5793` n `1136`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
