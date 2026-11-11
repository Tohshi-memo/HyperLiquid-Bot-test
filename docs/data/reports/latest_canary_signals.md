# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T19:37:29.858628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2016` n `13`; crypto_alt avg `0.0535` n `239`; crypto_major avg `0.1394` n `8`; equity avg `0.1028` n `161`; fx avg `-0.0021` n `6`; index avg `0.0086` n `27`; metal avg `0.0563` n `20`; unknown avg `4.7382` n `1264`
- 1h: commodity avg `-0.1931` n `13`; crypto_alt avg `-0.4957` n `239`; crypto_major avg `-0.4931` n `8`; equity avg `-0.5665` n `161`; fx avg `-0.0028` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0241` n `20`; unknown avg `24.1655` n `1256`
- 4h: commodity avg `-0.7012` n `13`; crypto_alt avg `-1.059` n `239`; crypto_major avg `-0.3896` n `8`; equity avg `0.2966` n `161`; fx avg `0.0067` n `6`; index avg `0.0988` n `27`; metal avg `-0.2267` n `20`; unknown avg `5.4617` n `1243`
- 24h: commodity avg `0.1703` n `13`; crypto_alt avg `0.9751` n `239`; crypto_major avg `1.4649` n `8`; equity avg `5.9119` n `161`; fx avg `-0.1402` n `6`; index avg `0.5698` n `27`; metal avg `0.0722` n `20`; unknown avg `11.4512` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
