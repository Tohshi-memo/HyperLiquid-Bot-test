# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T11:37:28.366232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0061` n `13`; crypto_alt avg `0.1816` n `238`; crypto_major avg `0.1196` n `8`; equity avg `0.0484` n `154`; fx avg `0.0171` n `6`; index avg `0.0151` n `27`; metal avg `0.0602` n `20`; unknown avg `0.3857` n `1239`
- 1h: commodity avg `0.1246` n `13`; crypto_alt avg `0.0859` n `238`; crypto_major avg `-0.08` n `8`; equity avg `-0.0486` n `154`; fx avg `0.0244` n `6`; index avg `0.0027` n `27`; metal avg `0.071` n `20`; unknown avg `0.0059` n `1235`
- 4h: commodity avg `0.0291` n `13`; crypto_alt avg `0.6812` n `238`; crypto_major avg `0.7547` n `8`; equity avg `0.2036` n `154`; fx avg `0.0655` n `6`; index avg `0.0174` n `27`; metal avg `0.0424` n `20`; unknown avg `82.5983` n `1186`
- 24h: commodity avg `0.2242` n `13`; crypto_alt avg `2.5024` n `238`; crypto_major avg `2.6226` n `8`; equity avg `3.1371` n `154`; fx avg `0.1254` n `6`; index avg `0.4314` n `27`; metal avg `0.2885` n `20`; unknown avg `6.8206` n `1070`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
