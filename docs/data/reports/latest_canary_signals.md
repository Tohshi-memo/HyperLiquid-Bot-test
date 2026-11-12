# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T18:52:33.850362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0486` n `13`; crypto_alt avg `-0.2356` n `239`; crypto_major avg `-0.4114` n `8`; equity avg `-0.52` n `162`; fx avg `0.0067` n `6`; index avg `-0.0511` n `27`; metal avg `-0.0612` n `20`; unknown avg `0.5473` n `1261`
- 1h: commodity avg `0.1908` n `13`; crypto_alt avg `-0.2448` n `239`; crypto_major avg `-0.4075` n `8`; equity avg `-0.7426` n `162`; fx avg `0.0181` n `6`; index avg `-0.0822` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.576` n `1255`
- 4h: commodity avg `0.4522` n `13`; crypto_alt avg `0.2479` n `239`; crypto_major avg `0.2974` n `8`; equity avg `0.1883` n `162`; fx avg `-0.0431` n `6`; index avg `0.0145` n `27`; metal avg `-0.0492` n `20`; unknown avg `56.6709` n `1229`
- 24h: commodity avg `0.4853` n `13`; crypto_alt avg `-3.0043` n `239`; crypto_major avg `-3.4161` n `8`; equity avg `-3.3422` n `162`; fx avg `-0.1358` n `6`; index avg `-0.2257` n `27`; metal avg `-0.7732` n `20`; unknown avg `16.1446` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
