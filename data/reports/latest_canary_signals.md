# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T11:52:33.497485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0527` n `13`; crypto_alt avg `0.0715` n `239`; crypto_major avg `0.0797` n `8`; equity avg `0.0842` n `168`; fx avg `0.0003` n `6`; index avg `0.0132` n `27`; metal avg `-0.015` n `20`; unknown avg `-0.1945` n `1267`
- 1h: commodity avg `0.1061` n `13`; crypto_alt avg `0.4568` n `239`; crypto_major avg `0.3844` n `8`; equity avg `0.441` n `168`; fx avg `-0.0158` n `6`; index avg `0.0577` n `27`; metal avg `0.0425` n `20`; unknown avg `1.0602` n `1263`
- 4h: commodity avg `0.1675` n `13`; crypto_alt avg `0.5001` n `239`; crypto_major avg `0.0547` n `8`; equity avg `0.08` n `168`; fx avg `0.0267` n `6`; index avg `0.0117` n `27`; metal avg `0.0586` n `20`; unknown avg `176.0234` n `1151`
- 24h: commodity avg `0.5957` n `13`; crypto_alt avg `4.4529` n `239`; crypto_major avg `3.6267` n `8`; equity avg `4.0122` n `168`; fx avg `0.0937` n `6`; index avg `0.3991` n `27`; metal avg `0.8077` n `20`; unknown avg `237.8055` n `1055`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
