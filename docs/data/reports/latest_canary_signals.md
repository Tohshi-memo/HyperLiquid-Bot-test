# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T14:22:25.046366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0553` n `12`; crypto_alt avg `-0.2763` n `228`; crypto_major avg `-0.2345` n `8`; equity avg `0.2587` n `72`; fx avg `0.0043` n `6`; index avg `0.0179` n `23`; metal avg `-0.0793` n `18`; unknown avg `0.9907` n `420`
- 1h: commodity avg `-0.1011` n `12`; crypto_alt avg `-0.3956` n `228`; crypto_major avg `-0.8378` n `8`; equity avg `-1.329` n `72`; fx avg `0.0066` n `6`; index avg `-0.4702` n `23`; metal avg `-0.441` n `18`; unknown avg `1.0233` n `420`
- 4h: commodity avg `-1.013` n `12`; crypto_alt avg `0.1652` n `228`; crypto_major avg `-0.9995` n `8`; equity avg `-1.2738` n `72`; fx avg `-0.0249` n `6`; index avg `-0.537` n `23`; metal avg `-0.8199` n `18`; unknown avg `0.7474` n `420`
- 24h: commodity avg `0.7061` n `12`; crypto_alt avg `0.0417` n `228`; crypto_major avg `-3.1141` n `8`; equity avg `-0.8065` n `72`; fx avg `0.0337` n `6`; index avg `0.0442` n `23`; metal avg `-1.4057` n `18`; unknown avg `-0.0214` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
