# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T06:37:30.146956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `0.2425` n `234`; crypto_major avg `0.2538` n `8`; equity avg `0.1846` n `137`; fx avg `0.0047` n `6`; index avg `0.0476` n `27`; metal avg `0.0098` n `20`; unknown avg `0.2563` n `921`
- 1h: commodity avg `-0.1965` n `12`; crypto_alt avg `0.2489` n `234`; crypto_major avg `0.2465` n `8`; equity avg `0.1677` n `137`; fx avg `-0.0284` n `6`; index avg `0.0613` n `27`; metal avg `0.0622` n `20`; unknown avg `0.2976` n `899`
- 4h: commodity avg `-0.168` n `12`; crypto_alt avg `0.7996` n `234`; crypto_major avg `0.1671` n `8`; equity avg `0.1614` n `137`; fx avg `-0.008` n `6`; index avg `0.0275` n `27`; metal avg `0.1626` n `20`; unknown avg `0.2544` n `890`
- 24h: commodity avg `-0.6446` n `12`; crypto_alt avg `2.9325` n `234`; crypto_major avg `1.6037` n `8`; equity avg `1.0138` n `137`; fx avg `0.0217` n `6`; index avg `0.0518` n `27`; metal avg `-0.1638` n `20`; unknown avg `0.6083` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
