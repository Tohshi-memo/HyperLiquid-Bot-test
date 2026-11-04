# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T04:52:27.947879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0272` n `13`; crypto_alt avg `1.0712` n `239`; crypto_major avg `0.7838` n `8`; equity avg `1.0641` n `158`; fx avg `0.0327` n `6`; index avg `0.1789` n `27`; metal avg `0.1982` n `20`; unknown avg `2.0405` n `1264`
- 1h: commodity avg `-0.0658` n `13`; crypto_alt avg `1.3091` n `239`; crypto_major avg `1.0064` n `8`; equity avg `1.008` n `158`; fx avg `0.0272` n `6`; index avg `0.1594` n `27`; metal avg `0.1964` n `20`; unknown avg `2.1619` n `1252`
- 4h: commodity avg `-0.3941` n `13`; crypto_alt avg `0.0337` n `239`; crypto_major avg `-0.0919` n `8`; equity avg `-1.4992` n `158`; fx avg `-0.0512` n `6`; index avg `-0.3005` n `27`; metal avg `0.0143` n `20`; unknown avg `1.4285` n `1254`
- 24h: commodity avg `-0.2986` n `13`; crypto_alt avg `0.475` n `239`; crypto_major avg `0.1139` n `8`; equity avg `0.04` n `158`; fx avg `0.148` n `6`; index avg `-0.1725` n `27`; metal avg `-0.1546` n `20`; unknown avg `0.8427` n `1049`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
