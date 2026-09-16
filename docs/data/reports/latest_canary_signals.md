# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T06:22:28.177571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `-0.0083` n `234`; crypto_major avg `0.0096` n `8`; equity avg `0.0524` n `137`; fx avg `-0.0305` n `6`; index avg `0.0366` n `27`; metal avg `0.0503` n `20`; unknown avg `0.3185` n `919`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.1762` n `234`; crypto_major avg `-0.0459` n `8`; equity avg `0.2383` n `137`; fx avg `-0.0129` n `6`; index avg `0.0637` n `27`; metal avg `-0.0124` n `20`; unknown avg `0.2931` n `889`
- 4h: commodity avg `-0.0564` n `12`; crypto_alt avg `0.2485` n `234`; crypto_major avg `0.2099` n `8`; equity avg `0.8476` n `137`; fx avg `-0.0359` n `6`; index avg `0.1387` n `27`; metal avg `0.24` n `20`; unknown avg `0.398` n `877`
- 24h: commodity avg `0.1746` n `12`; crypto_alt avg `-3.1547` n `234`; crypto_major avg `-3.0453` n `8`; equity avg `-0.1806` n `137`; fx avg `0.1496` n `6`; index avg `0.0862` n `27`; metal avg `0.4166` n `20`; unknown avg `18937.908` n `796`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
