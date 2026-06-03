# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T15:09:33.519758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.0969` n `228`; crypto_major avg `-0.2064` n `8`; equity avg `-0.2819` n `73`; fx avg `0.0111` n `6`; index avg `-0.0152` n `23`; metal avg `-0.1203` n `18`; unknown avg `1.0945` n `419`
- 1h: commodity avg `0.3207` n `12`; crypto_alt avg `0.1257` n `228`; crypto_major avg `-0.162` n `8`; equity avg `0.0562` n `73`; fx avg `0.0147` n `6`; index avg `0.161` n `23`; metal avg `-0.085` n `18`; unknown avg `0.9488` n `419`
- 4h: commodity avg `-0.5447` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `-1.0947` n `8`; equity avg `-1.5781` n `73`; fx avg `-0.0242` n `6`; index avg `-0.3823` n `23`; metal avg `-0.8366` n `18`; unknown avg `0.7922` n `419`
- 24h: commodity avg `1.2733` n `12`; crypto_alt avg `1.4386` n `228`; crypto_major avg `-2.2374` n `8`; equity avg `-0.9916` n `72`; fx avg `0.0258` n `6`; index avg `0.0996` n `23`; metal avg `-1.822` n `18`; unknown avg `0.345` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
