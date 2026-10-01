# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T05:37:34.763706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1592` n `13`; crypto_alt avg `0.014` n `234`; crypto_major avg `0.0531` n `8`; equity avg `0.0474` n `142`; fx avg `0.0005` n `6`; index avg `0.0095` n `26`; metal avg `0.0537` n `20`; unknown avg `-0.2177` n `974`
- 1h: commodity avg `0.1875` n `13`; crypto_alt avg `0.1618` n `234`; crypto_major avg `0.473` n `8`; equity avg `0.3598` n `142`; fx avg `-0.0101` n `6`; index avg `0.0773` n `26`; metal avg `0.1364` n `20`; unknown avg `0.5113` n `972`
- 4h: commodity avg `-0.1558` n `13`; crypto_alt avg `0.9303` n `234`; crypto_major avg `0.6095` n `8`; equity avg `0.9704` n `142`; fx avg `-0.0574` n `6`; index avg `0.2272` n `26`; metal avg `0.2364` n `20`; unknown avg `0.8151` n `966`
- 24h: commodity avg `-0.392` n `13`; crypto_alt avg `1.1546` n `234`; crypto_major avg `1.2268` n `8`; equity avg `0.9511` n `142`; fx avg `0.1567` n `6`; index avg `0.266` n `26`; metal avg `0.1227` n `20`; unknown avg `775.1491` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
