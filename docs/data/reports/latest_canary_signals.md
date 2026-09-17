# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T05:22:28.046288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `0.011` n `234`; crypto_major avg `-0.0541` n `8`; equity avg `-0.0731` n `137`; fx avg `-0.0002` n `6`; index avg `-0.0293` n `27`; metal avg `-0.0536` n `20`; unknown avg `11.9937` n `921`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `0.4717` n `234`; crypto_major avg `0.2132` n `8`; equity avg `-0.0475` n `137`; fx avg `0.0212` n `6`; index avg `-0.0401` n `27`; metal avg `-0.0486` n `20`; unknown avg `5.6613` n `913`
- 4h: commodity avg `0.0481` n `12`; crypto_alt avg `0.8242` n `234`; crypto_major avg `0.3231` n `8`; equity avg `0.1114` n `137`; fx avg `0.0252` n `6`; index avg `-0.0385` n `27`; metal avg `-0.0304` n `20`; unknown avg `0.1633` n `911`
- 24h: commodity avg `-0.3888` n `12`; crypto_alt avg `2.2324` n `234`; crypto_major avg `1.1677` n `8`; equity avg `1.1936` n `137`; fx avg `0.0332` n `6`; index avg `0.0802` n `27`; metal avg `-0.2662` n `20`; unknown avg `0.3194` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
