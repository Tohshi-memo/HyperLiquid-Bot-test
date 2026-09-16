# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T06:25:31.951408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0499` n `234`; crypto_major avg `-0.0406` n `8`; equity avg `0.0226` n `137`; fx avg `-0.0118` n `6`; index avg `0.0364` n `27`; metal avg `0.0388` n `20`; unknown avg `4.1529` n `919`
- 1h: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.2176` n `234`; crypto_major avg `-0.096` n `8`; equity avg `0.2085` n `137`; fx avg `0.0058` n `6`; index avg `0.0636` n `27`; metal avg `-0.0238` n `20`; unknown avg `3.8073` n `889`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `0.2068` n `234`; crypto_major avg `0.1596` n `8`; equity avg `0.8174` n `137`; fx avg `-0.0172` n `6`; index avg `0.1385` n `27`; metal avg `0.2285` n `20`; unknown avg `3.5034` n `877`
- 24h: commodity avg `0.1643` n `12`; crypto_alt avg `-3.1938` n `234`; crypto_major avg `-3.0937` n `8`; equity avg `-0.2105` n `137`; fx avg `0.1684` n `6`; index avg `0.086` n `27`; metal avg `0.4051` n `20`; unknown avg `18939.2213` n `796`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
