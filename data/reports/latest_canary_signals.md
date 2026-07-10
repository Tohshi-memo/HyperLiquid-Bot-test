# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T02:37:25.202792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.0213` n `229`; crypto_major avg `0.0609` n `8`; equity avg `0.1437` n `91`; fx avg `0.0393` n `6`; index avg `0.0475` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0144` n `765`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `0.4317` n `229`; crypto_major avg `0.6653` n `8`; equity avg `-0.0294` n `91`; fx avg `-0.0386` n `6`; index avg `-0.0234` n `25`; metal avg `0.1061` n `20`; unknown avg `0.3006` n `763`
- 4h: commodity avg `0.1032` n `12`; crypto_alt avg `0.7573` n `229`; crypto_major avg `0.9189` n `8`; equity avg `0.1258` n `91`; fx avg `0.0067` n `6`; index avg `-0.0358` n `25`; metal avg `0.1406` n `20`; unknown avg `0.1102` n `763`
- 24h: commodity avg `-1.0327` n `12`; crypto_alt avg `1.7182` n `229`; crypto_major avg `1.8007` n `8`; equity avg `1.5312` n `91`; fx avg `0.0313` n `6`; index avg `0.3714` n `25`; metal avg `0.7698` n `20`; unknown avg `0.0223` n `746`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
