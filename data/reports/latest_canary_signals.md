# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T11:22:29.067825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.0174` n `234`; crypto_major avg `0.0569` n `8`; equity avg `-0.0968` n `137`; fx avg `-0.0058` n `6`; index avg `-0.0038` n `27`; metal avg `0.0163` n `20`; unknown avg `-0.1294` n `921`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.1693` n `234`; crypto_major avg `0.0612` n `8`; equity avg `-0.0632` n `137`; fx avg `-0.0639` n `6`; index avg `0.0115` n `27`; metal avg `0.1388` n `20`; unknown avg `0.3748` n `919`
- 4h: commodity avg `-0.0841` n `12`; crypto_alt avg `-0.0189` n `234`; crypto_major avg `-0.2489` n `8`; equity avg `0.3137` n `137`; fx avg `0.0041` n `6`; index avg `0.0668` n `27`; metal avg `0.0711` n `20`; unknown avg `0.7379` n `911`
- 24h: commodity avg `-0.6112` n `12`; crypto_alt avg `2.9672` n `234`; crypto_major avg `1.1571` n `8`; equity avg `1.4339` n `137`; fx avg `0.0551` n `6`; index avg `0.1562` n `27`; metal avg `-0.0754` n `20`; unknown avg `0.2823` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
