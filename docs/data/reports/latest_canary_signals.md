# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T04:37:26.415712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `0.1073` n `229`; crypto_major avg `0.0264` n `8`; equity avg `0.0224` n `88`; fx avg `0.0` n `6`; index avg `-0.0047` n `25`; metal avg `0.0049` n `20`; unknown avg `3.3333` n `765`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.2595` n `229`; crypto_major avg `0.3233` n `8`; equity avg `0.0847` n `88`; fx avg `0.0015` n `6`; index avg `0.0022` n `25`; metal avg `0.0136` n `20`; unknown avg `3.3943` n `765`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.4822` n `229`; crypto_major avg `-0.4442` n `8`; equity avg `0.1459` n `88`; fx avg `0.0045` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.5189` n `763`
- 24h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.7946` n `229`; crypto_major avg `-1.1266` n `8`; equity avg `0.183` n `88`; fx avg `-0.0084` n `6`; index avg `0.02` n `25`; metal avg `0.0824` n `20`; unknown avg `-0.8346` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
