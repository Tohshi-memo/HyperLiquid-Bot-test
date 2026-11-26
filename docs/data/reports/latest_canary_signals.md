# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T06:07:26.193632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0645` n `13`; crypto_alt avg `-0.1109` n `239`; crypto_major avg `-0.2996` n `8`; equity avg `-0.318` n `168`; fx avg `0.0015` n `6`; index avg `-0.045` n `27`; metal avg `-0.0747` n `20`; unknown avg `3.0529` n `1239`
- 1h: commodity avg `-0.0806` n `13`; crypto_alt avg `0.0418` n `239`; crypto_major avg `-0.3847` n `8`; equity avg `-0.6708` n `168`; fx avg `0.0051` n `6`; index avg `-0.0797` n `27`; metal avg `-0.179` n `20`; unknown avg `3.1722` n `1239`
- 4h: commodity avg `0.0109` n `13`; crypto_alt avg `-0.1281` n `239`; crypto_major avg `-0.2367` n `8`; equity avg `-0.2988` n `168`; fx avg `0.0168` n `6`; index avg `-0.036` n `27`; metal avg `0.0353` n `20`; unknown avg `4.6956` n `1221`
- 24h: commodity avg `0.5297` n `13`; crypto_alt avg `3.2323` n `239`; crypto_major avg `2.9256` n `8`; equity avg `2.4349` n `168`; fx avg `0.022` n `6`; index avg `0.1693` n `27`; metal avg `0.7961` n `20`; unknown avg `766.2093` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
