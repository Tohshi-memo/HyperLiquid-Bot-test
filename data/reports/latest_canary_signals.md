# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T14:37:42.633798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `0.1766` n `234`; crypto_major avg `-0.0553` n `8`; equity avg `0.1423` n `141`; fx avg `0.0124` n `6`; index avg `0.0146` n `26`; metal avg `-0.0586` n `20`; unknown avg `0.0311` n `911`
- 1h: commodity avg `0.1056` n `12`; crypto_alt avg `0.3114` n `234`; crypto_major avg `-0.2976` n `8`; equity avg `0.8176` n `141`; fx avg `-0.0178` n `6`; index avg `0.0643` n `26`; metal avg `0.0547` n `20`; unknown avg `222.4417` n `909`
- 4h: commodity avg `-0.1951` n `12`; crypto_alt avg `1.1903` n `234`; crypto_major avg `0.4733` n `8`; equity avg `0.8666` n `141`; fx avg `-0.0205` n `6`; index avg `0.061` n `26`; metal avg `0.0071` n `20`; unknown avg `2.3202` n `903`
- 24h: commodity avg `-0.7708` n `12`; crypto_alt avg `2.7476` n `234`; crypto_major avg `1.1509` n `8`; equity avg `1.4646` n `141`; fx avg `-0.1212` n `6`; index avg `0.105` n `26`; metal avg `-0.0538` n `20`; unknown avg `13.1652` n `796`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
