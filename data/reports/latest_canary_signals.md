# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T07:52:31.841679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `13`; crypto_alt avg `-0.0434` n `239`; crypto_major avg `-0.1063` n `8`; equity avg `-0.0604` n `168`; fx avg `-0.0197` n `6`; index avg `-0.0139` n `27`; metal avg `-0.1038` n `20`; unknown avg `158.445` n `1267`
- 1h: commodity avg `0.0688` n `13`; crypto_alt avg `0.1859` n `239`; crypto_major avg `0.1945` n `8`; equity avg `0.159` n `168`; fx avg `0.0138` n `6`; index avg `0.0246` n `27`; metal avg `-0.0157` n `20`; unknown avg `0.8708` n `1263`
- 4h: commodity avg `-0.2743` n `13`; crypto_alt avg `-0.4619` n `239`; crypto_major avg `-0.6133` n `8`; equity avg `-0.4748` n `168`; fx avg `0.0122` n `6`; index avg `-0.046` n `27`; metal avg `-0.2083` n `20`; unknown avg `0.8561` n `1221`
- 24h: commodity avg `0.7431` n `13`; crypto_alt avg `3.078` n `239`; crypto_major avg `3.3621` n `8`; equity avg `3.2783` n `168`; fx avg `0.0882` n `6`; index avg `0.2644` n `27`; metal avg `0.6202` n `20`; unknown avg `759.3472` n `1033`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
