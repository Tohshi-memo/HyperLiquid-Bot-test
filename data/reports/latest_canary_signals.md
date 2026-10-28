# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T03:52:38.214574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.043` n `13`; crypto_alt avg `0.0945` n `238`; crypto_major avg `-0.0078` n `8`; equity avg `0.0421` n `154`; fx avg `0.0161` n `6`; index avg `0.003` n `27`; metal avg `0.0144` n `20`; unknown avg `0.8595` n `1236`
- 1h: commodity avg `0.0657` n `13`; crypto_alt avg `0.1287` n `238`; crypto_major avg `0.24` n `8`; equity avg `0.3577` n `154`; fx avg `0.0229` n `6`; index avg `0.0194` n `27`; metal avg `-0.0125` n `20`; unknown avg `161.7895` n `1228`
- 4h: commodity avg `0.2072` n `13`; crypto_alt avg `0.528` n `238`; crypto_major avg `0.4715` n `8`; equity avg `1.066` n `154`; fx avg `0.1424` n `6`; index avg `0.1496` n `27`; metal avg `-0.1453` n `20`; unknown avg `0.9824` n `1216`
- 24h: commodity avg `0.036` n `13`; crypto_alt avg `2.5246` n `237`; crypto_major avg `2.2396` n `8`; equity avg `2.7857` n `154`; fx avg `0.0878` n `6`; index avg `0.4913` n `27`; metal avg `0.1917` n `20`; unknown avg `7.0335` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
