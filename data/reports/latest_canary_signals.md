# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T06:37:28.045891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0656` n `13`; crypto_alt avg `0.2166` n `239`; crypto_major avg `-0.0106` n `8`; equity avg `-0.003` n `166`; fx avg `-0.0038` n `6`; index avg `0.0033` n `27`; metal avg `0.0435` n `20`; unknown avg `158.0134` n `1264`
- 1h: commodity avg `-0.2067` n `13`; crypto_alt avg `0.1471` n `239`; crypto_major avg `-0.1928` n `8`; equity avg `-0.0334` n `166`; fx avg `0.0167` n `6`; index avg `-0.0425` n `27`; metal avg `-0.0326` n `20`; unknown avg `161.3302` n `1242`
- 4h: commodity avg `-0.1057` n `13`; crypto_alt avg `1.713` n `239`; crypto_major avg `1.4494` n `8`; equity avg `1.5768` n `166`; fx avg `0.0412` n `6`; index avg `0.0349` n `27`; metal avg `0.4247` n `20`; unknown avg `0.077` n `1225`
- 24h: commodity avg `-0.4766` n `13`; crypto_alt avg `2.3501` n `239`; crypto_major avg `2.9326` n `8`; equity avg `2.3353` n `166`; fx avg `0.2208` n `6`; index avg `0.1487` n `27`; metal avg `0.5224` n `20`; unknown avg `339.0982` n `1021`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
