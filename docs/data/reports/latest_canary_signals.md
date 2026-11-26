# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T10:07:28.498175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `13`; crypto_alt avg `-0.0007` n `239`; crypto_major avg `-0.0217` n `8`; equity avg `0.0291` n `168`; fx avg `-0.0035` n `6`; index avg `0.0096` n `27`; metal avg `-0.0179` n `20`; unknown avg `1.8513` n `1257`
- 1h: commodity avg `0.0445` n `13`; crypto_alt avg `-0.0068` n `239`; crypto_major avg `-0.0925` n `8`; equity avg `-0.1295` n `168`; fx avg `0.0204` n `6`; index avg `-0.0149` n `27`; metal avg `-0.0315` n `20`; unknown avg `0.8999` n `1255`
- 4h: commodity avg `-0.188` n `13`; crypto_alt avg `0.0114` n `239`; crypto_major avg `0.0829` n `8`; equity avg `-0.0198` n `168`; fx avg `0.0524` n `6`; index avg `-0.0068` n `27`; metal avg `0.0304` n `20`; unknown avg `360.3576` n `1151`
- 24h: commodity avg `0.2835` n `13`; crypto_alt avg `3.6702` n `239`; crypto_major avg `3.6501` n `8`; equity avg `3.7645` n `168`; fx avg `0.0945` n `6`; index avg `0.3078` n `27`; metal avg `0.672` n `20`; unknown avg `200.6406` n `999`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
