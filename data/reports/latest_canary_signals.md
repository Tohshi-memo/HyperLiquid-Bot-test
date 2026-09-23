# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T23:22:30.199219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.0747` n `234`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0322` n `141`; fx avg `0.0014` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0072` n `20`; unknown avg `1.0806` n `945`
- 1h: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.1143` n `234`; crypto_major avg `-0.1351` n `8`; equity avg `-0.0753` n `141`; fx avg `-0.0018` n `6`; index avg `-0.0364` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.8548` n `943`
- 4h: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.035` n `234`; crypto_major avg `0.192` n `8`; equity avg `-0.065` n `141`; fx avg `-0.0109` n `6`; index avg `0.0027` n `26`; metal avg `0.0509` n `20`; unknown avg `-0.6516` n `845`
- 24h: commodity avg `0.5024` n `12`; crypto_alt avg `-4.8939` n `234`; crypto_major avg `-3.6597` n `8`; equity avg `-1.6632` n `140`; fx avg `-0.003` n `6`; index avg `-0.3739` n `26`; metal avg `-0.8498` n `20`; unknown avg `585.3801` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
