# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T11:37:27.674022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `-0.151` n `234`; crypto_major avg `-0.2065` n `8`; equity avg `0.0044` n `137`; fx avg `0.0129` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0686` n `20`; unknown avg `0.289` n `921`
- 1h: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.0457` n `234`; crypto_major avg `-0.17` n `8`; equity avg `-0.0569` n `137`; fx avg `-0.0486` n `6`; index avg `0.0123` n `27`; metal avg `0.0545` n `20`; unknown avg `0.5883` n `919`
- 4h: commodity avg `-0.1052` n `12`; crypto_alt avg `-0.1391` n `234`; crypto_major avg `-0.4076` n `8`; equity avg `0.2911` n `137`; fx avg `0.007` n `6`; index avg `0.0516` n `27`; metal avg `-0.0967` n `20`; unknown avg `0.5497` n `911`
- 24h: commodity avg `-0.5612` n `12`; crypto_alt avg `2.6163` n `234`; crypto_major avg `0.6708` n `8`; equity avg `1.3027` n `137`; fx avg `0.1069` n `6`; index avg `0.1263` n `27`; metal avg `-0.1569` n `20`; unknown avg `0.5298` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
