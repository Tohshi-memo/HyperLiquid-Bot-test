# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T18:52:31.422941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `-0.1823` n `239`; crypto_major avg `-0.2266` n `8`; equity avg `-0.1943` n `168`; fx avg `-0.0158` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0544` n `20`; unknown avg `158.7747` n `1265`
- 1h: commodity avg `0.1995` n `13`; crypto_alt avg `-0.1199` n `239`; crypto_major avg `0.0215` n `8`; equity avg `0.0794` n `168`; fx avg `-0.0152` n `6`; index avg `0.001` n `27`; metal avg `-0.0076` n `20`; unknown avg `162.1519` n `1245`
- 4h: commodity avg `0.2316` n `13`; crypto_alt avg `-0.8742` n `239`; crypto_major avg `-0.8429` n `8`; equity avg `-1.5054` n `168`; fx avg `0.0138` n `6`; index avg `-0.0984` n `27`; metal avg `-0.7281` n `20`; unknown avg `162.526` n `1227`
- 24h: commodity avg `0.6314` n `13`; crypto_alt avg `-3.6626` n `239`; crypto_major avg `-3.3132` n `8`; equity avg `-3.6512` n `167`; fx avg `0.2608` n `6`; index avg `-0.2167` n `27`; metal avg `-1.1722` n `20`; unknown avg `178.9585` n `1113`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
