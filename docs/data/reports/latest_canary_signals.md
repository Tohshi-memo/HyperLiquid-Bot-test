# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T11:52:30.392604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.2469` n `234`; crypto_major avg `0.2257` n `8`; equity avg `0.1153` n `137`; fx avg `0.0213` n `6`; index avg `0.0255` n `27`; metal avg `0.0112` n `20`; unknown avg `0.4677` n `919`
- 1h: commodity avg `-0.0456` n `12`; crypto_alt avg `0.5035` n `234`; crypto_major avg `0.6842` n `8`; equity avg `0.3145` n `137`; fx avg `-0.0313` n `6`; index avg `0.0423` n `27`; metal avg `0.0551` n `20`; unknown avg `0.8665` n `917`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.7246` n `234`; crypto_major avg `0.9191` n `8`; equity avg `0.3498` n `137`; fx avg `-0.0097` n `6`; index avg `0.0704` n `27`; metal avg `0.1094` n `20`; unknown avg `0.0794` n `911`
- 24h: commodity avg `0.2355` n `12`; crypto_alt avg `-2.0322` n `234`; crypto_major avg `-1.9367` n `8`; equity avg `0.0131` n `137`; fx avg `0.0896` n `6`; index avg `0.0818` n `27`; metal avg `0.5035` n `20`; unknown avg `18892.3203` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
