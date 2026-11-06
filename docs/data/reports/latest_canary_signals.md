# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T01:07:25.024937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `13`; crypto_alt avg `0.1104` n `239`; crypto_major avg `0.0613` n `8`; equity avg `0.0045` n `158`; fx avg `-0.0071` n `6`; index avg `0.0149` n `27`; metal avg `-0.0498` n `20`; unknown avg `-0.0106` n `1252`
- 1h: commodity avg `-0.0046` n `13`; crypto_alt avg `0.9773` n `239`; crypto_major avg `0.5877` n `8`; equity avg `1.0097` n `158`; fx avg `0.0077` n `6`; index avg `0.0757` n `27`; metal avg `-0.0287` n `20`; unknown avg `19.8241` n `1252`
- 4h: commodity avg `0.0722` n `13`; crypto_alt avg `0.2506` n `239`; crypto_major avg `0.1754` n `8`; equity avg `1.0845` n `158`; fx avg `0.0065` n `6`; index avg `0.0793` n `27`; metal avg `0.0335` n `20`; unknown avg `0.4497` n `1216`
- 24h: commodity avg `0.9675` n `13`; crypto_alt avg `-4.3022` n `239`; crypto_major avg `-5.1513` n `8`; equity avg `-6.7911` n `158`; fx avg `0.1191` n `6`; index avg `-1.0108` n `27`; metal avg `-0.0706` n `20`; unknown avg `231.687` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2311`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
