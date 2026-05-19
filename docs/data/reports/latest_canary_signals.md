# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T04:52:19.210048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.1535` n `228`; crypto_major avg `0.1563` n `8`; equity avg `-0.0194` n `66`; fx avg `-0.0035` n `6`; index avg `0.023` n `23`; metal avg `0.0421` n `18`; unknown avg `-0.0091` n `383`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.1836` n `228`; crypto_major avg `0.0411` n `8`; equity avg `-0.221` n `66`; fx avg `0.0083` n `6`; index avg `-0.1778` n `23`; metal avg `-0.1005` n `18`; unknown avg `0.0107` n `383`
- 4h: commodity avg `0.1948` n `12`; crypto_alt avg `-0.2414` n `228`; crypto_major avg `-0.4196` n `8`; equity avg `-0.6374` n `66`; fx avg `0.0832` n `6`; index avg `-0.44` n `23`; metal avg `-1.0314` n `18`; unknown avg `-0.5163` n `383`
- 24h: commodity avg `0.1094` n `12`; crypto_alt avg `0.9602` n `228`; crypto_major avg `0.2921` n `8`; equity avg `-0.8525` n `66`; fx avg `0.2534` n `6`; index avg `-0.435` n `23`; metal avg `0.3973` n `18`; unknown avg `0.6356` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
