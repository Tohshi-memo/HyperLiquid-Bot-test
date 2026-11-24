# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T15:22:31.416949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1232` n `13`; crypto_alt avg `-0.3674` n `239`; crypto_major avg `-0.3294` n `8`; equity avg `-0.6258` n `167`; fx avg `-0.0178` n `6`; index avg `-0.0587` n `27`; metal avg `-0.1589` n `20`; unknown avg `2.3497` n `1264`
- 1h: commodity avg `-0.037` n `13`; crypto_alt avg `-1.0556` n `239`; crypto_major avg `-1.2501` n `8`; equity avg `-1.5042` n `167`; fx avg `-0.0166` n `6`; index avg `-0.0728` n `27`; metal avg `-0.2436` n `20`; unknown avg `254.6828` n `1262`
- 4h: commodity avg `0.2986` n `13`; crypto_alt avg `-1.2609` n `239`; crypto_major avg `-0.9751` n `8`; equity avg `-1.1317` n `166`; fx avg `0.0687` n `6`; index avg `-0.0645` n `27`; metal avg `-0.2258` n `20`; unknown avg `51.9059` n `1246`
- 24h: commodity avg `0.5141` n `13`; crypto_alt avg `-5.9729` n `239`; crypto_major avg `-6.8055` n `8`; equity avg `-5.2773` n `166`; fx avg `0.1567` n `6`; index avg `-0.427` n `27`; metal avg `-1.1387` n `20`; unknown avg `24.5469` n `1140`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
