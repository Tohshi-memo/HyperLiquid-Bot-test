# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T06:22:27.070502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0519` n `12`; crypto_alt avg `0.0783` n `229`; crypto_major avg `0.0334` n `8`; equity avg `-0.011` n `91`; fx avg `0.0046` n `6`; index avg `0.0109` n `25`; metal avg `-0.01` n `20`; unknown avg `0.5687` n `763`
- 1h: commodity avg `0.1829` n `12`; crypto_alt avg `0.4915` n `229`; crypto_major avg `0.4585` n `8`; equity avg `0.5332` n `91`; fx avg `0.0164` n `6`; index avg `0.127` n `25`; metal avg `0.041` n `20`; unknown avg `0.5976` n `745`
- 4h: commodity avg `0.0829` n `12`; crypto_alt avg `-0.7321` n `229`; crypto_major avg `-0.8491` n `8`; equity avg `-0.4637` n `91`; fx avg `-0.0198` n `6`; index avg `-0.0818` n `25`; metal avg `-0.3016` n `20`; unknown avg `14.9763` n `745`
- 24h: commodity avg `0.2292` n `12`; crypto_alt avg `0.4491` n `229`; crypto_major avg `-0.4785` n `8`; equity avg `-1.3207` n `90`; fx avg `-0.0093` n `6`; index avg `-0.2883` n `25`; metal avg `-0.3732` n `20`; unknown avg `0.0863` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
