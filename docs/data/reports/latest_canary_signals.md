# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T02:52:32.687493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `-0.1486` n `228`; crypto_major avg `-0.2546` n `8`; equity avg `-0.0843` n `86`; fx avg `-0.0086` n `6`; index avg `0.0037` n `23`; metal avg `-0.0752` n `20`; unknown avg `-0.1606` n `764`
- 1h: commodity avg `0.0675` n `12`; crypto_alt avg `-0.0939` n `228`; crypto_major avg `-0.2504` n `8`; equity avg `-0.2623` n `86`; fx avg `-0.0167` n `6`; index avg `0.0009` n `23`; metal avg `-0.1303` n `20`; unknown avg `-0.0509` n `748`
- 4h: commodity avg `-0.0206` n `12`; crypto_alt avg `0.0777` n `228`; crypto_major avg `0.0523` n `8`; equity avg `-0.5115` n `86`; fx avg `0.0921` n `6`; index avg `-0.0628` n `23`; metal avg `-0.3014` n `20`; unknown avg `0.1963` n `732`
- 24h: commodity avg `-0.3648` n `12`; crypto_alt avg `-2.2176` n `228`; crypto_major avg `-2.0633` n `8`; equity avg `-0.0439` n `86`; fx avg `0.0766` n `6`; index avg `0.6204` n `23`; metal avg `-1.5919` n `20`; unknown avg `-0.3668` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
