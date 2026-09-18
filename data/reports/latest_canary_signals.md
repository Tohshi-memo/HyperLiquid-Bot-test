# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T00:07:33.348817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `0.0576` n `234`; crypto_major avg `0.0242` n `8`; equity avg `-0.093` n `140`; fx avg `0.0236` n `6`; index avg `-0.0608` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.3769` n `917`
- 1h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.3834` n `234`; crypto_major avg `0.1557` n `8`; equity avg `-0.0685` n `140`; fx avg `0.0408` n `6`; index avg `-0.0733` n `26`; metal avg `0.0223` n `20`; unknown avg `0.2917` n `917`
- 4h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.681` n `234`; crypto_major avg `0.3117` n `8`; equity avg `-0.1142` n `140`; fx avg `0.0405` n `6`; index avg `-0.0969` n `26`; metal avg `0.0306` n `20`; unknown avg `0.7103` n `815`
- 24h: commodity avg `-0.1715` n `12`; crypto_alt avg `3.4254` n `234`; crypto_major avg `2.0044` n `8`; equity avg `1.4475` n `138`; fx avg `0.0782` n `6`; index avg `0.1602` n `26`; metal avg `0.5007` n `20`; unknown avg `2.3478` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
