# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T07:22:32.940254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `-0.4004` n `234`; crypto_major avg `-0.2826` n `8`; equity avg `-0.0386` n `137`; fx avg `-0.0202` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0143` n `20`; unknown avg `0.1368` n `919`
- 1h: commodity avg `-0.0643` n `12`; crypto_alt avg `-0.1765` n `234`; crypto_major avg `-0.0769` n `8`; equity avg `0.1535` n `137`; fx avg `-0.0475` n `6`; index avg `-0.0038` n `27`; metal avg `0.0546` n `20`; unknown avg `0.9422` n `917`
- 4h: commodity avg `-0.0252` n `12`; crypto_alt avg `-0.411` n `234`; crypto_major avg `-0.3476` n `8`; equity avg `0.3231` n `137`; fx avg `-0.0499` n `6`; index avg `0.0323` n `27`; metal avg `-0.0144` n `20`; unknown avg `0.153` n `881`
- 24h: commodity avg `0.0601` n `12`; crypto_alt avg `-3.2484` n `234`; crypto_major avg `-2.8676` n `8`; equity avg `0.0421` n `137`; fx avg `0.087` n `6`; index avg `0.1188` n `27`; metal avg `0.544` n `20`; unknown avg `18891.539` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
