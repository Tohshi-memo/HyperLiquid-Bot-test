# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T22:52:33.382270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.0285` n `234`; crypto_major avg `-0.1348` n `8`; equity avg `-0.0064` n `137`; fx avg `0.0038` n `6`; index avg `0.0012` n `27`; metal avg `-0.0253` n `20`; unknown avg `0.7676` n `919`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.3241` n `234`; crypto_major avg `-0.4662` n `8`; equity avg `0.1864` n `137`; fx avg `-0.0029` n `6`; index avg `0.0558` n `27`; metal avg `0.0182` n `20`; unknown avg `0.0322` n `829`
- 4h: commodity avg `0.0188` n `12`; crypto_alt avg `0.4305` n `234`; crypto_major avg `-0.2329` n `8`; equity avg `0.4062` n `137`; fx avg `0.0691` n `6`; index avg `0.0195` n `27`; metal avg `-0.0868` n `20`; unknown avg `-0.8188` n `753`
- 24h: commodity avg `-0.6013` n `12`; crypto_alt avg `-0.0589` n `234`; crypto_major avg `0.1312` n `8`; equity avg `1.1812` n `137`; fx avg `0.078` n `6`; index avg `0.0768` n `27`; metal avg `-0.2883` n `20`; unknown avg `-1.3451` n `723`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
