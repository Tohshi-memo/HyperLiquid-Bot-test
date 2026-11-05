# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T14:07:33.665083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0983` n `13`; crypto_alt avg `0.033` n `239`; crypto_major avg `0.016` n `8`; equity avg `-0.0406` n `158`; fx avg `0.0138` n `6`; index avg `-0.0241` n `27`; metal avg `-0.0184` n `20`; unknown avg `0.1013` n `1250`
- 1h: commodity avg `-0.0716` n `13`; crypto_alt avg `0.1607` n `239`; crypto_major avg `-0.0131` n `8`; equity avg `0.0119` n `158`; fx avg `-0.012` n `6`; index avg `0.0008` n `27`; metal avg `0.1424` n `20`; unknown avg `-0.1283` n `1253`
- 4h: commodity avg `0.2207` n `13`; crypto_alt avg `-1.0943` n `239`; crypto_major avg `-1.0486` n `8`; equity avg `-1.194` n `158`; fx avg `0.0345` n `6`; index avg `-0.0811` n `27`; metal avg `0.2453` n `20`; unknown avg `186.7403` n `1229`
- 24h: commodity avg `-0.7754` n `13`; crypto_alt avg `0.4792` n `239`; crypto_major avg `1.2328` n `8`; equity avg `-2.6353` n `158`; fx avg `-0.028` n `6`; index avg `-0.2736` n `27`; metal avg `0.8648` n `20`; unknown avg `214.8138` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2339`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
