# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T13:52:28.709545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.0758` n `239`; crypto_major avg `0.0009` n `8`; equity avg `-0.047` n `158`; fx avg `-0.0214` n `6`; index avg `0.0019` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.0044` n `1261`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `0.2406` n `239`; crypto_major avg `0.1468` n `8`; equity avg `0.0301` n `158`; fx avg `-0.0135` n `6`; index avg `0.0189` n `27`; metal avg `0.0056` n `20`; unknown avg `-0.0256` n `1255`
- 4h: commodity avg `0.0393` n `13`; crypto_alt avg `-0.1245` n `239`; crypto_major avg `-0.1953` n `8`; equity avg `0.0262` n `158`; fx avg `0.0363` n `6`; index avg `0.0067` n `27`; metal avg `0.0045` n `20`; unknown avg `-0.1543` n `1249`
- 24h: commodity avg `-0.0137` n `13`; crypto_alt avg `-1.241` n `239`; crypto_major avg `-0.4881` n `8`; equity avg `-0.533` n `158`; fx avg `0.0396` n `6`; index avg `-0.045` n `27`; metal avg `0.142` n `20`; unknown avg `0.0216` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
