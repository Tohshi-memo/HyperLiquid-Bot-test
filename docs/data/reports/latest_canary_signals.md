# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T17:04:08.784821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.311` n `234`; crypto_major avg `-0.1473` n `8`; equity avg `-0.0774` n `141`; fx avg `0.0039` n `6`; index avg `-0.0024` n `26`; metal avg `0.0135` n `20`; unknown avg `0.3431` n `960`
- 1h: commodity avg `-0.2022` n `12`; crypto_alt avg `0.2509` n `234`; crypto_major avg `0.1514` n `8`; equity avg `0.2204` n `141`; fx avg `0.0056` n `6`; index avg `0.0707` n `26`; metal avg `0.0792` n `20`; unknown avg `14.3385` n `960`
- 4h: commodity avg `-0.2227` n `12`; crypto_alt avg `-1.0975` n `234`; crypto_major avg `-0.4543` n `8`; equity avg `-0.7207` n `141`; fx avg `0.035` n `6`; index avg `-0.0981` n `26`; metal avg `-0.0601` n `20`; unknown avg `85.4584` n `904`
- 24h: commodity avg `-0.3403` n `12`; crypto_alt avg `-3.1939` n `234`; crypto_major avg `-1.5135` n `8`; equity avg `-3.1447` n `141`; fx avg `0.0331` n `6`; index avg `-0.2735` n `26`; metal avg `-1.0192` n `20`; unknown avg `21.0475` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
