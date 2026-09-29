# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T15:07:33.061114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `-0.5694` n `234`; crypto_major avg `-0.711` n `8`; equity avg `-0.2343` n `141`; fx avg `0.0086` n `6`; index avg `-0.0614` n `26`; metal avg `-0.0525` n `20`; unknown avg `1.8745` n `933`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.0095` n `234`; crypto_major avg `-0.6325` n `8`; equity avg `0.2836` n `141`; fx avg `0.0114` n `6`; index avg `0.0176` n `26`; metal avg `0.0042` n `20`; unknown avg `212.5994` n `901`
- 4h: commodity avg `-0.1687` n `12`; crypto_alt avg `0.4025` n `234`; crypto_major avg `-0.3798` n `8`; equity avg `0.3708` n `141`; fx avg `0.0152` n `6`; index avg `-0.0358` n `26`; metal avg `-0.0441` n `20`; unknown avg `229.0985` n `895`
- 24h: commodity avg `-0.8431` n `12`; crypto_alt avg `3.0328` n `234`; crypto_major avg `1.0171` n `8`; equity avg `1.417` n `141`; fx avg `-0.1302` n `6`; index avg `0.132` n `26`; metal avg `0.0173` n `20`; unknown avg `13.5965` n `788`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
