# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T06:23:02.370674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `-0.0192` n `234`; crypto_major avg `-0.0517` n `8`; equity avg `-0.0045` n `137`; fx avg `-0.0224` n `6`; index avg `0.0091` n `27`; metal avg `-0.0168` n `20`; unknown avg `0.6178` n `921`
- 1h: commodity avg `-0.2067` n `12`; crypto_alt avg `0.0219` n `234`; crypto_major avg `-0.1312` n `8`; equity avg `-0.1751` n `137`; fx avg `-0.0199` n `6`; index avg `-0.0162` n `27`; metal avg `0.0794` n `20`; unknown avg `0.7331` n `899`
- 4h: commodity avg `-0.1753` n `12`; crypto_alt avg `1.0359` n `234`; crypto_major avg `0.3492` n `8`; equity avg `0.1871` n `137`; fx avg `-0.0151` n `6`; index avg `-0.0004` n `27`; metal avg `0.1578` n `20`; unknown avg `1.0763` n `890`
- 24h: commodity avg `-0.576` n `12`; crypto_alt avg `2.4751` n `234`; crypto_major avg `1.1322` n `8`; equity avg `0.8039` n `137`; fx avg `0.0069` n `6`; index avg `0.0004` n `27`; metal avg `-0.1638` n `20`; unknown avg `0.6713` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
