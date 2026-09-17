# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T03:52:31.727509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.0405` n `234`; crypto_major avg `-0.1187` n `8`; equity avg `0.0687` n `137`; fx avg `0.0042` n `6`; index avg `0.0126` n `27`; metal avg `0.0272` n `20`; unknown avg `0.3459` n `921`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.2021` n `234`; crypto_major avg `0.0736` n `8`; equity avg `0.0622` n `137`; fx avg `0.0078` n `6`; index avg `0.0129` n `27`; metal avg `0.1346` n `20`; unknown avg `0.0451` n `919`
- 4h: commodity avg `0.1116` n `12`; crypto_alt avg `0.6205` n `234`; crypto_major avg `0.3867` n `8`; equity avg `0.1068` n `137`; fx avg `0.0269` n `6`; index avg `-0.0178` n `27`; metal avg `0.2347` n `20`; unknown avg `0.7727` n `911`
- 24h: commodity avg `-0.416` n `12`; crypto_alt avg `2.2738` n `234`; crypto_major avg `1.3888` n `8`; equity avg `1.0909` n `137`; fx avg `0.0114` n `6`; index avg `0.091` n `27`; metal avg `-0.1928` n `20`; unknown avg `0.9229` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
