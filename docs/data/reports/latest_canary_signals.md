# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T05:07:27.781542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.5369` n `239`; crypto_major avg `-0.4324` n `8`; equity avg `-0.1706` n `168`; fx avg `0.001` n `6`; index avg `-0.0159` n `27`; metal avg `-0.0261` n `20`; unknown avg `-0.2222` n `1251`
- 1h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.9076` n `239`; crypto_major avg `-0.5495` n `8`; equity avg `-0.0791` n `168`; fx avg `0.0003` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0157` n `20`; unknown avg `201.7038` n `1247`
- 4h: commodity avg `0.046` n `13`; crypto_alt avg `-1.378` n `239`; crypto_major avg `-0.5189` n `8`; equity avg `0.139` n `168`; fx avg `-0.0034` n `6`; index avg `0.0011` n `27`; metal avg `0.0084` n `20`; unknown avg `42.0111` n `1239`
- 24h: commodity avg `-0.8274` n `13`; crypto_alt avg `-2.5957` n `239`; crypto_major avg `-2.5013` n `8`; equity avg `0.0797` n `168`; fx avg `-0.1349` n `6`; index avg `0.0145` n `27`; metal avg `0.0185` n `20`; unknown avg `214.5546` n `977`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
