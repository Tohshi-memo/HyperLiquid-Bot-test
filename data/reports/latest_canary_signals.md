# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T07:52:32.576619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.1097` n `234`; crypto_major avg `-0.1422` n `8`; equity avg `-0.048` n `137`; fx avg `0.0032` n `6`; index avg `-0.012` n `27`; metal avg `-0.0912` n `20`; unknown avg `0.5611` n `919`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.2514` n `234`; crypto_major avg `-0.1901` n `8`; equity avg `0.0899` n `137`; fx avg `-0.0343` n `6`; index avg `-0.0138` n `27`; metal avg `-0.0227` n `20`; unknown avg `7.0305` n `917`
- 4h: commodity avg `-0.1105` n `12`; crypto_alt avg `-0.2459` n `234`; crypto_major avg `-0.2087` n `8`; equity avg `0.2176` n `137`; fx avg `-0.0437` n `6`; index avg `0.0308` n `27`; metal avg `-0.0068` n `20`; unknown avg `5.6256` n `881`
- 24h: commodity avg `-0.059` n `12`; crypto_alt avg `-2.8567` n `234`; crypto_major avg `-2.6635` n `8`; equity avg `0.1364` n `137`; fx avg `0.1054` n `6`; index avg `0.1512` n `27`; metal avg `0.6072` n `20`; unknown avg `18889.3622` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
