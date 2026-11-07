# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T01:37:27.959326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `-0.0569` n `239`; crypto_major avg `0.0631` n `8`; equity avg `0.1081` n `158`; fx avg `-0.0012` n `6`; index avg `0.0067` n `27`; metal avg `0.0072` n `20`; unknown avg `5.5333` n `1261`
- 1h: commodity avg `-0.0353` n `13`; crypto_alt avg `0.0708` n `239`; crypto_major avg `0.138` n `8`; equity avg `0.0195` n `158`; fx avg `0.0055` n `6`; index avg `0.0112` n `27`; metal avg `0.0186` n `20`; unknown avg `6.7578` n `1255`
- 4h: commodity avg `0.0318` n `13`; crypto_alt avg `-0.0225` n `239`; crypto_major avg `0.4364` n `8`; equity avg `0.0039` n `158`; fx avg `-0.0113` n `6`; index avg `-0.0023` n `27`; metal avg `0.0587` n `20`; unknown avg `0.4318` n `1227`
- 24h: commodity avg `0.0015` n `13`; crypto_alt avg `1.0196` n `239`; crypto_major avg `-0.0614` n `8`; equity avg `1.7298` n `158`; fx avg `-0.0823` n `6`; index avg `0.2878` n `27`; metal avg `0.0531` n `20`; unknown avg `8.4085` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
