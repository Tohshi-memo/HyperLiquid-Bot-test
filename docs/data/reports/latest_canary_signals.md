# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T00:37:26.271271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.108` n `12`; crypto_alt avg `0.2446` n `229`; crypto_major avg `0.0692` n `8`; equity avg `0.0476` n `91`; fx avg `0.0001` n `6`; index avg `0.0435` n `25`; metal avg `0.1081` n `20`; unknown avg `0.0415` n `763`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `0.1775` n `229`; crypto_major avg `-0.0682` n `8`; equity avg `0.5806` n `91`; fx avg `0.0359` n `6`; index avg `0.0864` n `25`; metal avg `0.0632` n `20`; unknown avg `0.8872` n `763`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.3431` n `229`; crypto_major avg `-0.4282` n `8`; equity avg `0.1098` n `91`; fx avg `0.0547` n `6`; index avg `0.0478` n `25`; metal avg `0.0197` n `20`; unknown avg `-0.0812` n `763`
- 24h: commodity avg `0.8451` n `12`; crypto_alt avg `-2.5042` n `229`; crypto_major avg `-1.8446` n `8`; equity avg `-2.3017` n `91`; fx avg `-0.2183` n `6`; index avg `-0.3289` n `25`; metal avg `-0.4387` n `20`; unknown avg `-0.2278` n `729`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
