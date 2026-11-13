# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T01:07:24.838504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `0.0645` n `239`; crypto_major avg `-0.1037` n `8`; equity avg `0.0283` n `162`; fx avg `-0.0382` n `6`; index avg `-0.0042` n `27`; metal avg `0.0385` n `20`; unknown avg `11.8413` n `1256`
- 1h: commodity avg `-0.0566` n `13`; crypto_alt avg `-0.084` n `239`; crypto_major avg `-0.3442` n `8`; equity avg `-0.3489` n `162`; fx avg `-0.0275` n `6`; index avg `-0.0155` n `27`; metal avg `-0.0105` n `20`; unknown avg `3.5401` n `1259`
- 4h: commodity avg `-0.1064` n `13`; crypto_alt avg `0.4198` n `239`; crypto_major avg `0.1712` n `8`; equity avg `0.7107` n `162`; fx avg `-0.0319` n `6`; index avg `0.0871` n `27`; metal avg `0.134` n `20`; unknown avg `12.7173` n `1209`
- 24h: commodity avg `0.8658` n `13`; crypto_alt avg `-0.5663` n `239`; crypto_major avg `-1.7592` n `8`; equity avg `0.0608` n `162`; fx avg `-0.105` n `6`; index avg `0.1286` n `27`; metal avg `-0.6913` n `20`; unknown avg `52.4996` n `1119`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
