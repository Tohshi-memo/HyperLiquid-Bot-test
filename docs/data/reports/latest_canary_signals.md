# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T21:33:04.627460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `12`; crypto_alt avg `-0.0625` n `230`; crypto_major avg `-0.0113` n `8`; equity avg `0.0099` n `98`; fx avg `-0.0023` n `6`; index avg `-0.0028` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0162` n `773`
- 1h: commodity avg `0.0685` n `12`; crypto_alt avg `0.0041` n `230`; crypto_major avg `-0.04` n `8`; equity avg `0.2081` n `98`; fx avg `-0.0002` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.1549` n `773`
- 4h: commodity avg `0.0627` n `12`; crypto_alt avg `-0.3266` n `230`; crypto_major avg `-0.2867` n `8`; equity avg `-0.0168` n `98`; fx avg `0.0035` n `6`; index avg `-0.0485` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.1349` n `773`
- 24h: commodity avg `0.5681` n `12`; crypto_alt avg `-0.5014` n `230`; crypto_major avg `-0.7001` n `8`; equity avg `-0.8961` n `98`; fx avg `-0.0264` n `6`; index avg `-0.1512` n `25`; metal avg `0.2704` n `20`; unknown avg `1.0218` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
