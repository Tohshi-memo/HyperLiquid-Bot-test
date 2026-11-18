# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T19:37:45.999454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1009` n `13`; crypto_alt avg `-0.1509` n `239`; crypto_major avg `-0.2437` n `8`; equity avg `-0.2852` n `164`; fx avg `-0.0055` n `6`; index avg `-0.0303` n `27`; metal avg `-0.0645` n `20`; unknown avg `0.1591` n `1265`
- 1h: commodity avg `0.2632` n `13`; crypto_alt avg `-0.1342` n `239`; crypto_major avg `-0.6084` n `8`; equity avg `-0.6272` n `164`; fx avg `-0.0087` n `6`; index avg `-0.0694` n `27`; metal avg `-0.1682` n `20`; unknown avg `-0.3547` n `1263`
- 4h: commodity avg `0.2153` n `13`; crypto_alt avg `-0.3221` n `239`; crypto_major avg `-0.4878` n `8`; equity avg `-0.059` n `164`; fx avg `0.0041` n `6`; index avg `0.0004` n `27`; metal avg `-0.1235` n `20`; unknown avg `-0.5549` n `1257`
- 24h: commodity avg `-0.0604` n `13`; crypto_alt avg `0.3708` n `239`; crypto_major avg `-0.4021` n `8`; equity avg `0.0931` n `164`; fx avg `-0.1849` n `6`; index avg `0.0316` n `27`; metal avg `-1.1995` n `20`; unknown avg `-0.2748` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
