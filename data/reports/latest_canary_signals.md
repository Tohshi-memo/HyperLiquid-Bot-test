# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T22:24:53.283376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0017` n `234`; crypto_major avg `0.0412` n `8`; equity avg `0.115` n `137`; fx avg `0.0046` n `6`; index avg `0.0181` n `27`; metal avg `-0.01` n `20`; unknown avg `-0.2517` n `853`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.4355` n `234`; crypto_major avg `-0.4863` n `8`; equity avg `0.1834` n `137`; fx avg `-0.0033` n `6`; index avg `0.0227` n `27`; metal avg `-0.03` n `20`; unknown avg `0.1657` n `845`
- 4h: commodity avg `0.0099` n `12`; crypto_alt avg `0.2048` n `234`; crypto_major avg `-0.4069` n `8`; equity avg `-0.2403` n `137`; fx avg `0.0799` n `6`; index avg `-0.1553` n `27`; metal avg `-0.3633` n `20`; unknown avg `-0.59` n `761`
- 24h: commodity avg `-0.6215` n `12`; crypto_alt avg `0.5624` n `234`; crypto_major avg `0.8171` n `8`; equity avg `1.1231` n `137`; fx avg `0.073` n `6`; index avg `0.053` n `27`; metal avg `-0.3196` n `20`; unknown avg `-0.9324` n `723`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
