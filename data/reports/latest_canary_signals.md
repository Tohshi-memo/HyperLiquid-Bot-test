# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T06:52:32.997827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0905` n `229`; crypto_major avg `0.1643` n `8`; equity avg `0.0843` n `91`; fx avg `-0.0011` n `6`; index avg `0.0043` n `25`; metal avg `0.0333` n `20`; unknown avg `-0.0251` n `763`
- 1h: commodity avg `0.1196` n `12`; crypto_alt avg `0.2826` n `229`; crypto_major avg `0.3579` n `8`; equity avg `0.1192` n `91`; fx avg `0.0322` n `6`; index avg `0.0231` n `25`; metal avg `0.1766` n `20`; unknown avg `0.1921` n `745`
- 4h: commodity avg `0.1449` n `12`; crypto_alt avg `0.0748` n `229`; crypto_major avg `0.1328` n `8`; equity avg `-0.0252` n `91`; fx avg `-0.0036` n `6`; index avg `-0.029` n `25`; metal avg `-0.1139` n `20`; unknown avg `13.0749` n `745`
- 24h: commodity avg `0.2587` n `12`; crypto_alt avg `0.7704` n `229`; crypto_major avg `-0.0513` n `8`; equity avg `-1.2945` n `90`; fx avg `-0.0147` n `6`; index avg `-0.3275` n `25`; metal avg `-0.2375` n `20`; unknown avg `-0.3227` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
