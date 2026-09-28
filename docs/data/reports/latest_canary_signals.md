# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T17:37:33.896430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0668` n `12`; crypto_alt avg `-0.1134` n `234`; crypto_major avg `-0.2518` n `8`; equity avg `-0.1231` n `141`; fx avg `0.0093` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1834` n `963`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `-0.0764` n `234`; crypto_major avg `-0.0825` n `8`; equity avg `-0.1891` n `141`; fx avg `0.016` n `6`; index avg `-0.025` n `26`; metal avg `0.0078` n `20`; unknown avg `3.4106` n `960`
- 4h: commodity avg `-0.3436` n `12`; crypto_alt avg `-0.5777` n `234`; crypto_major avg `-0.0521` n `8`; equity avg `-0.4036` n `141`; fx avg `0.0484` n `6`; index avg `-0.0294` n `26`; metal avg `0.0211` n `20`; unknown avg `96.5993` n `904`
- 24h: commodity avg `-0.4545` n `12`; crypto_alt avg `-2.8491` n `234`; crypto_major avg `-1.2032` n `8`; equity avg `-3.0395` n `141`; fx avg `0.0426` n `6`; index avg `-0.2669` n `26`; metal avg `-0.9435` n `20`; unknown avg `23.0066` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
