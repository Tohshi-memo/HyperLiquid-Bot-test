# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T07:07:28.749920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0105` n `229`; crypto_major avg `-0.0373` n `8`; equity avg `-0.003` n `88`; fx avg `0.0015` n `6`; index avg `0.0001` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0135` n `765`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.1831` n `229`; crypto_major avg `0.1057` n `8`; equity avg `-0.0029` n `88`; fx avg `0.0119` n `6`; index avg `0.0207` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0537` n `763`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.1414` n `229`; crypto_major avg `0.0029` n `8`; equity avg `0.0677` n `88`; fx avg `0.0089` n `6`; index avg `0.0469` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.024` n `731`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.7168` n `229`; crypto_major avg `-0.6922` n `8`; equity avg `0.1638` n `88`; fx avg `-0.0021` n `6`; index avg `0.0481` n `25`; metal avg `0.0782` n `20`; unknown avg `-1.2018` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
