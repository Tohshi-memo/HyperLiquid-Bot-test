# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T02:37:20.735288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `0.1294` n `228`; crypto_major avg `0.0753` n `8`; equity avg `0.074` n `72`; fx avg `0.0078` n `6`; index avg `0.0182` n `23`; metal avg `0.0601` n `18`; unknown avg `-0.2016` n `420`
- 1h: commodity avg `-0.1306` n `12`; crypto_alt avg `0.0898` n `228`; crypto_major avg `0.1432` n `8`; equity avg `-0.0446` n `72`; fx avg `0.0157` n `6`; index avg `0.0708` n `23`; metal avg `0.1819` n `18`; unknown avg `-0.0251` n `419`
- 4h: commodity avg `0.1784` n `12`; crypto_alt avg `-0.3844` n `228`; crypto_major avg `-0.433` n `8`; equity avg `-0.4372` n `72`; fx avg `0.0225` n `6`; index avg `0.2435` n `23`; metal avg `-0.2511` n `18`; unknown avg `-0.5829` n `419`
- 24h: commodity avg `0.561` n `12`; crypto_alt avg `-3.6377` n `228`; crypto_major avg `-5.8249` n `8`; equity avg `1.3948` n `72`; fx avg `0.042` n `6`; index avg `1.5705` n `23`; metal avg `0.0317` n `18`; unknown avg `-0.9914` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
