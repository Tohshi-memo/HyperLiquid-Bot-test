# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T07:37:30.731987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.016` n `234`; crypto_major avg `-0.0283` n `8`; equity avg `0.0036` n `137`; fx avg `0.0004` n `6`; index avg `0.0043` n `27`; metal avg `0.0341` n `20`; unknown avg `-0.0868` n `919`
- 1h: commodity avg `-0.1056` n `12`; crypto_alt avg `0.0039` n `234`; crypto_major avg `0.1059` n `8`; equity avg `0.18` n `137`; fx avg `-0.0369` n `6`; index avg `0.0042` n `27`; metal avg `0.0788` n `20`; unknown avg `-0.103` n `917`
- 4h: commodity avg `-0.1126` n `12`; crypto_alt avg `-0.1548` n `234`; crypto_major avg `-0.0722` n `8`; equity avg `0.4148` n `137`; fx avg `-0.047` n `6`; index avg `0.0687` n `27`; metal avg `0.0922` n `20`; unknown avg `0.1222` n `881`
- 24h: commodity avg `-0.0035` n `12`; crypto_alt avg `-3.113` n `234`; crypto_major avg `-2.7734` n `8`; equity avg `0.0373` n `137`; fx avg `0.1042` n `6`; index avg `0.1329` n `27`; metal avg `0.5887` n `20`; unknown avg `18889.6146` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
