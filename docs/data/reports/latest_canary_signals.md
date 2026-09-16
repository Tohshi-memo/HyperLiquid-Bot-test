# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T09:22:39.799870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `0.0528` n `234`; crypto_major avg `0.0973` n `8`; equity avg `-0.0129` n `137`; fx avg `0.0074` n `6`; index avg `-0.0294` n `27`; metal avg `-0.0146` n `20`; unknown avg `-0.0222` n `919`
- 1h: commodity avg `0.159` n `12`; crypto_alt avg `0.2512` n `234`; crypto_major avg `0.3778` n `8`; equity avg `0.0693` n `137`; fx avg `0.0261` n `6`; index avg `0.0001` n `27`; metal avg `-0.05` n `20`; unknown avg `-0.0343` n `911`
- 4h: commodity avg `0.0556` n `12`; crypto_alt avg `-0.5216` n `234`; crypto_major avg `-0.2351` n `8`; equity avg `0.307` n `137`; fx avg `-0.0003` n `6`; index avg `0.0452` n `27`; metal avg `-0.0809` n `20`; unknown avg `6.1322` n `881`
- 24h: commodity avg `0.1144` n `12`; crypto_alt avg `-2.9576` n `234`; crypto_major avg `-2.6922` n `8`; equity avg `0.34` n `137`; fx avg `0.098` n `6`; index avg `0.1808` n `27`; metal avg `0.5783` n `20`; unknown avg `18892.9684` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
