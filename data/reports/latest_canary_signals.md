# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T16:37:41.757093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `0.1929` n `234`; crypto_major avg `0.0969` n `8`; equity avg `0.0096` n `140`; fx avg `0.0007` n `6`; index avg `0.0005` n `26`; metal avg `0.0312` n `20`; unknown avg `-0.0182` n `934`
- 1h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.2199` n `234`; crypto_major avg `-0.4144` n `8`; equity avg `-0.0243` n `140`; fx avg `0.0156` n `6`; index avg `0.0116` n `26`; metal avg `-0.0097` n `20`; unknown avg `-0.2324` n `920`
- 4h: commodity avg `0.4691` n `12`; crypto_alt avg `0.3771` n `234`; crypto_major avg `-0.1407` n `8`; equity avg `0.6527` n `140`; fx avg `-0.0372` n `6`; index avg `0.074` n `26`; metal avg `-0.0715` n `20`; unknown avg `2.7423` n `886`
- 24h: commodity avg `0.3212` n `12`; crypto_alt avg `1.032` n `234`; crypto_major avg `1.0417` n `8`; equity avg `0.6807` n `140`; fx avg `-0.27` n `6`; index avg `0.0778` n `26`; metal avg `-0.0719` n `20`; unknown avg `22.6362` n `828`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
