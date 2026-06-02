# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T13:37:30.221337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2376` n `12`; crypto_alt avg `-0.0651` n `228`; crypto_major avg `-0.0167` n `8`; equity avg `-0.4324` n `69`; fx avg `-0.0053` n `6`; index avg `-0.0381` n `23`; metal avg `0.0094` n `18`; unknown avg `0.8439` n `422`
- 1h: commodity avg `0.1558` n `12`; crypto_alt avg `0.4603` n `228`; crypto_major avg `0.0666` n `8`; equity avg `-0.4114` n `69`; fx avg `0.0046` n `6`; index avg `-0.0608` n `23`; metal avg `-0.4085` n `18`; unknown avg `0.9383` n `422`
- 4h: commodity avg `0.0922` n `12`; crypto_alt avg `0.9893` n `228`; crypto_major avg `0.2463` n `8`; equity avg `-0.401` n `69`; fx avg `0.0238` n `6`; index avg `0.022` n `23`; metal avg `-0.3212` n `18`; unknown avg `0.7546` n `422`
- 24h: commodity avg `-0.8` n `12`; crypto_alt avg `0.7474` n `228`; crypto_major avg `-1.2726` n `8`; equity avg `0.902` n `69`; fx avg `0.1867` n `6`; index avg `0.4374` n `23`; metal avg `1.2213` n `18`; unknown avg `0.2164` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
