# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T13:37:30.915491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0801` n `13`; crypto_alt avg `0.1233` n `238`; crypto_major avg `0.1174` n `8`; equity avg `-0.0716` n `154`; fx avg `0.0278` n `6`; index avg `0.0179` n `27`; metal avg `-0.0247` n `20`; unknown avg `2.5889` n `1237`
- 1h: commodity avg `0.0737` n `13`; crypto_alt avg `0.1683` n `238`; crypto_major avg `0.065` n `8`; equity avg `-0.2823` n `154`; fx avg `0.0115` n `6`; index avg `0.0338` n `27`; metal avg `-0.0632` n `20`; unknown avg `3.4965` n `1233`
- 4h: commodity avg `0.2453` n `13`; crypto_alt avg `-0.7442` n `238`; crypto_major avg `-0.7575` n `8`; equity avg `-0.2544` n `154`; fx avg `0.0585` n `6`; index avg `0.0746` n `27`; metal avg `-0.0029` n `20`; unknown avg `1.496` n `1229`
- 24h: commodity avg `0.3594` n `13`; crypto_alt avg `1.0708` n `238`; crypto_major avg `0.9947` n `8`; equity avg `1.956` n `154`; fx avg `0.1518` n `6`; index avg `0.4085` n `27`; metal avg `0.148` n `20`; unknown avg `6.8402` n `1068`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
