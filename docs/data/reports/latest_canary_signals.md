# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T23:52:28.989447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.2084` n `239`; crypto_major avg `0.2084` n `8`; equity avg `-0.148` n `161`; fx avg `-0.009` n `6`; index avg `-0.0467` n `27`; metal avg `-0.0099` n `20`; unknown avg `0.5885` n `1262`
- 1h: commodity avg `-0.0177` n `13`; crypto_alt avg `-0.0185` n `239`; crypto_major avg `-0.013` n `8`; equity avg `-0.3422` n `161`; fx avg `-0.0133` n `6`; index avg `-0.018` n `27`; metal avg `-0.0961` n `20`; unknown avg `5.7435` n `1256`
- 4h: commodity avg `0.0632` n `13`; crypto_alt avg `-1.2042` n `239`; crypto_major avg `-0.9828` n `8`; equity avg `-1.7122` n `161`; fx avg `-0.0297` n `6`; index avg `-0.1728` n `27`; metal avg `-0.1684` n `20`; unknown avg `3.1517` n `1204`
- 24h: commodity avg `0.2206` n `13`; crypto_alt avg `-1.2554` n `239`; crypto_major avg `-0.1724` n `8`; equity avg `2.4241` n `161`; fx avg `-0.1738` n `6`; index avg `0.2565` n `27`; metal avg `-0.2282` n `20`; unknown avg `2.8013` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
