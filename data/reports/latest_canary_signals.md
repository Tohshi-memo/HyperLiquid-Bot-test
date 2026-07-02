# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T15:52:31.365955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6175` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `-0.1142` n `229`; crypto_major avg `-0.1276` n `8`; equity avg `-0.4672` n `88`; fx avg `0.0046` n `6`; index avg `-0.1069` n `25`; metal avg `-0.1297` n `20`; unknown avg `0.3005` n `763`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `0.0258` n `229`; crypto_major avg `0.1009` n `8`; equity avg `-0.4179` n `88`; fx avg `-0.0638` n `6`; index avg `-0.094` n `25`; metal avg `-0.0227` n `20`; unknown avg `0.1287` n `763`
- 4h: commodity avg `0.1674` n `12`; crypto_alt avg `-0.115` n `229`; crypto_major avg `0.4141` n `8`; equity avg `-1.2034` n `88`; fx avg `-0.028` n `6`; index avg `-0.2192` n `25`; metal avg `0.552` n `20`; unknown avg `-0.0461` n `763`
- 24h: commodity avg `-0.2144` n `12`; crypto_alt avg `1.1771` n `228`; crypto_major avg `2.3432` n `8`; equity avg `-2.5535` n `88`; fx avg `-0.0809` n `6`; index avg `-0.5405` n `25`; metal avg `0.5823` n `20`; unknown avg `1.6177` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
