# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T16:37:28.492169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `0.2194` n `239`; crypto_major avg `0.3265` n `8`; equity avg `0.6454` n `158`; fx avg `0.0054` n `6`; index avg `0.0723` n `27`; metal avg `-0.0169` n `20`; unknown avg `0.6796` n `1257`
- 1h: commodity avg `0.213` n `13`; crypto_alt avg `0.1496` n `239`; crypto_major avg `0.4831` n `8`; equity avg `1.1275` n `158`; fx avg `0.0109` n `6`; index avg `0.1219` n `27`; metal avg `0.0796` n `20`; unknown avg `46.8139` n `1247`
- 4h: commodity avg `-0.1277` n `13`; crypto_alt avg `-0.0562` n `239`; crypto_major avg `-0.2707` n `8`; equity avg `-0.8261` n `158`; fx avg `-0.0225` n `6`; index avg `0.0503` n `27`; metal avg `-0.0225` n `20`; unknown avg `54.2862` n `1245`
- 24h: commodity avg `0.1793` n `13`; crypto_alt avg `1.5727` n `239`; crypto_major avg `-1.2697` n `8`; equity avg `0.5036` n `158`; fx avg `-0.0854` n `6`; index avg `0.0164` n `27`; metal avg `-0.3603` n `20`; unknown avg `52.624` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
