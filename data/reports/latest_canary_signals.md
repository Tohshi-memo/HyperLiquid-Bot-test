# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T00:37:27.359125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0899` n `13`; crypto_alt avg `0.0504` n `237`; crypto_major avg `0.1045` n `8`; equity avg `-0.2037` n `154`; fx avg `0.0223` n `6`; index avg `-0.0344` n `27`; metal avg `-0.0437` n `20`; unknown avg `0.4615` n `1236`
- 1h: commodity avg `0.0165` n `13`; crypto_alt avg `0.2418` n `237`; crypto_major avg `0.3329` n `8`; equity avg `0.338` n `154`; fx avg `0.0079` n `6`; index avg `0.0748` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.0862` n `1228`
- 4h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.6817` n `237`; crypto_major avg `0.7813` n `8`; equity avg `0.5687` n `154`; fx avg `-0.0019` n `6`; index avg `0.1375` n `27`; metal avg `-0.0112` n `20`; unknown avg `1.1297` n `1202`
- 24h: commodity avg `0.0141` n `13`; crypto_alt avg `0.3427` n `237`; crypto_major avg `0.6285` n `8`; equity avg `1.4338` n `153`; fx avg `-0.0407` n `6`; index avg `0.0436` n `27`; metal avg `-0.0047` n `20`; unknown avg `760.0328` n `970`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
