# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T08:37:30.409763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0935` n `12`; crypto_alt avg `-0.1338` n `234`; crypto_major avg `-0.0646` n `8`; equity avg `-0.0471` n `137`; fx avg `0.0137` n `6`; index avg `-0.0085` n `27`; metal avg `-0.0825` n `20`; unknown avg `-0.0077` n `913`
- 1h: commodity avg `0.0929` n `12`; crypto_alt avg `-0.4966` n `234`; crypto_major avg `-0.4745` n `8`; equity avg `-0.1752` n `137`; fx avg `0.0287` n `6`; index avg `-0.0272` n `27`; metal avg `-0.1779` n `20`; unknown avg `-0.0036` n `911`
- 4h: commodity avg `0.0355` n `12`; crypto_alt avg `-1.0996` n `234`; crypto_major avg `-0.8595` n `8`; equity avg `0.129` n `137`; fx avg `-0.0007` n `6`; index avg `0.0371` n `27`; metal avg `-0.1109` n `20`; unknown avg `6.1613` n `881`
- 24h: commodity avg `0.0528` n `12`; crypto_alt avg `-3.292` n `234`; crypto_major avg `-2.9502` n `8`; equity avg `0.1806` n `137`; fx avg `0.0958` n `6`; index avg `0.1532` n `27`; metal avg `0.5081` n `20`; unknown avg `18892.4645` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
