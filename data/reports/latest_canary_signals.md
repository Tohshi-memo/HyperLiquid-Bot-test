# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T15:22:28.690193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.037` n `231`; crypto_major avg `-0.2881` n `8`; equity avg `0.0417` n `122`; fx avg `-0.0005` n `6`; index avg `0.0258` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0206` n `793`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.2192` n `231`; crypto_major avg `-0.8492` n `8`; equity avg `0.0305` n `122`; fx avg `0.0077` n `6`; index avg `0.0292` n `25`; metal avg `0.0155` n `20`; unknown avg `0.3651` n `793`
- 4h: commodity avg `0.0114` n `12`; crypto_alt avg `1.7013` n `231`; crypto_major avg `0.1561` n `8`; equity avg `0.1965` n `122`; fx avg `-0.0065` n `6`; index avg `0.0482` n `25`; metal avg `0.0332` n `20`; unknown avg `2.8085` n `793`
- 24h: commodity avg `0.0649` n `12`; crypto_alt avg `2.9273` n `231`; crypto_major avg `1.9073` n `8`; equity avg `0.6741` n `122`; fx avg `0.0501` n `6`; index avg `0.0814` n `25`; metal avg `0.066` n `20`; unknown avg `8.4234` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
