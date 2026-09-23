# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T07:52:34.576128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0755` n `234`; crypto_major avg `-0.0661` n `8`; equity avg `-0.0153` n `140`; fx avg `0.0036` n `6`; index avg `-0.0084` n `26`; metal avg `0.0191` n `20`; unknown avg `0.0981` n `945`
- 1h: commodity avg `0.1134` n `12`; crypto_alt avg `-0.634` n `234`; crypto_major avg `-0.5074` n `8`; equity avg `-0.1337` n `140`; fx avg `0.0626` n `6`; index avg `-0.0379` n `26`; metal avg `-0.1431` n `20`; unknown avg `0.0831` n `943`
- 4h: commodity avg `0.1466` n `12`; crypto_alt avg `-0.5693` n `234`; crypto_major avg `-0.7402` n `8`; equity avg `0.0011` n `140`; fx avg `0.1321` n `6`; index avg `0.0107` n `26`; metal avg `-0.2278` n `20`; unknown avg `0.4043` n `921`
- 24h: commodity avg `-0.0379` n `12`; crypto_alt avg `3.5914` n `234`; crypto_major avg `1.9171` n `8`; equity avg `1.358` n `140`; fx avg `-0.0826` n `6`; index avg `0.1665` n `26`; metal avg `0.1274` n `20`; unknown avg `2.0447` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
