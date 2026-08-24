# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T10:07:25.204333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.2487` n `231`; crypto_major avg `0.1792` n `8`; equity avg `0.0943` n `122`; fx avg `0.0094` n `6`; index avg `0.0104` n `25`; metal avg `0.0187` n `20`; unknown avg `0.0134` n `793`
- 1h: commodity avg `0.0712` n `12`; crypto_alt avg `0.3577` n `231`; crypto_major avg `0.4196` n `8`; equity avg `0.0918` n `122`; fx avg `0.0029` n `6`; index avg `0.008` n `25`; metal avg `0.0475` n `20`; unknown avg `0.1678` n `793`
- 4h: commodity avg `0.1186` n `12`; crypto_alt avg `0.4444` n `231`; crypto_major avg `0.3273` n `8`; equity avg `0.3237` n `122`; fx avg `0.0378` n `6`; index avg `0.0543` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.4456` n `793`
- 24h: commodity avg `-0.1925` n `12`; crypto_alt avg `2.1284` n `231`; crypto_major avg `0.6826` n `8`; equity avg `-1.1567` n `122`; fx avg `-0.1415` n `6`; index avg `-0.1062` n `25`; metal avg `0.1776` n `20`; unknown avg `5.601` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
