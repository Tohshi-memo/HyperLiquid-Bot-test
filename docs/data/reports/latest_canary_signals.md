# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T07:52:28.448973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0574` n `13`; crypto_alt avg `0.0564` n `239`; crypto_major avg `-0.0298` n `8`; equity avg `0.1086` n `158`; fx avg `-0.0026` n `6`; index avg `0.007` n `27`; metal avg `0.0271` n `20`; unknown avg `-0.1108` n `1264`
- 1h: commodity avg `-0.0705` n `13`; crypto_alt avg `0.3016` n `239`; crypto_major avg `0.1377` n `8`; equity avg `0.09` n `158`; fx avg `0.0126` n `6`; index avg `0.0143` n `27`; metal avg `0.0543` n `20`; unknown avg `-0.0725` n `1256`
- 4h: commodity avg `0.2251` n `13`; crypto_alt avg `3.2966` n `239`; crypto_major avg `2.17` n `8`; equity avg `3.2674` n `158`; fx avg `0.0759` n `6`; index avg `0.4751` n `27`; metal avg `1.0217` n `20`; unknown avg `2.4062` n `1234`
- 24h: commodity avg `-0.25` n `13`; crypto_alt avg `2.7763` n `239`; crypto_major avg `1.3493` n `8`; equity avg `2.3299` n `158`; fx avg `0.1574` n `6`; index avg `0.1193` n `27`; metal avg `0.8579` n `20`; unknown avg `191.4499` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2261`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
