# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T06:07:30.796554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1023` n `13`; crypto_alt avg `-0.3977` n `239`; crypto_major avg `-0.4232` n `8`; equity avg `-0.1323` n `160`; fx avg `-0.0107` n `6`; index avg `-0.0208` n `27`; metal avg `-0.0186` n `20`; unknown avg `0.3749` n `1241`
- 1h: commodity avg `0.0275` n `13`; crypto_alt avg `-0.0896` n `239`; crypto_major avg `-0.0655` n `8`; equity avg `0.3547` n `160`; fx avg `-0.0819` n `6`; index avg `0.0796` n `27`; metal avg `0.0565` n `20`; unknown avg `0.9542` n `1233`
- 4h: commodity avg `-0.1112` n `13`; crypto_alt avg `0.2852` n `239`; crypto_major avg `0.0136` n `8`; equity avg `0.1259` n `160`; fx avg `-0.1026` n `6`; index avg `0.0294` n `27`; metal avg `0.0132` n `20`; unknown avg `1.1654` n `1217`
- 24h: commodity avg `-0.5848` n `13`; crypto_alt avg `1.3792` n `239`; crypto_major avg `0.1526` n `8`; equity avg `4.3597` n `160`; fx avg `-0.0148` n `6`; index avg `0.495` n `27`; metal avg `0.1708` n `20`; unknown avg `191.1363` n `1065`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
