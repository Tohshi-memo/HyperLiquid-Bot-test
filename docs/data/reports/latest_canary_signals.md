# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T08:07:25.343748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.1137` n `229`; crypto_major avg `-0.1896` n `8`; equity avg `-0.0443` n `91`; fx avg `0.0121` n `6`; index avg `0.0034` n `25`; metal avg `0.0442` n `20`; unknown avg `-0.0276` n `763`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.4021` n `229`; crypto_major avg `-0.5342` n `8`; equity avg `-0.2005` n `91`; fx avg `-0.0596` n `6`; index avg `-0.023` n `25`; metal avg `0.0636` n `20`; unknown avg `-0.1582` n `763`
- 4h: commodity avg `0.2217` n `12`; crypto_alt avg `-0.0562` n `229`; crypto_major avg `0.0109` n `8`; equity avg `0.2896` n `91`; fx avg `-0.0008` n `6`; index avg `0.0337` n `25`; metal avg `-0.074` n `20`; unknown avg `6.6776` n `745`
- 24h: commodity avg `0.5264` n `12`; crypto_alt avg `0.0749` n `229`; crypto_major avg `-0.8837` n `8`; equity avg `-1.5924` n `90`; fx avg `-0.0523` n `6`; index avg `-0.3883` n `25`; metal avg `-0.533` n `20`; unknown avg `-0.5125` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
