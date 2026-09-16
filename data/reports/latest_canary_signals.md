# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T12:00:25.256053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `-0.0722` n `234`; crypto_major avg `-0.0974` n `8`; equity avg `-0.0319` n `137`; fx avg `-0.0077` n `6`; index avg `0.0042` n `27`; metal avg `-0.0391` n `20`; unknown avg `0.0572` n `917`
- 1h: commodity avg `-0.0721` n `12`; crypto_alt avg `0.3751` n `234`; crypto_major avg `0.4481` n `8`; equity avg `0.1881` n `137`; fx avg `-0.0354` n `6`; index avg `0.0323` n `27`; metal avg `-0.0236` n `20`; unknown avg `9.733` n `917`
- 4h: commodity avg `-0.1158` n `12`; crypto_alt avg `0.9801` n `234`; crypto_major avg `1.1608` n `8`; equity avg `0.4918` n `137`; fx avg `-0.0249` n `6`; index avg `0.0986` n `27`; metal avg `0.1132` n `20`; unknown avg `0.2358` n `911`
- 24h: commodity avg `0.1251` n `12`; crypto_alt avg `-2.2611` n `234`; crypto_major avg `-2.146` n `8`; equity avg `-0.0243` n `137`; fx avg `0.0662` n `6`; index avg `0.0879` n `27`; metal avg `0.4865` n `20`; unknown avg `18890.8249` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
