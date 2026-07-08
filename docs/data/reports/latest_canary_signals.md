# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T00:56:46.648463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0479` n `12`; crypto_alt avg `0.0593` n `229`; crypto_major avg `-0.0421` n `8`; equity avg `0.5908` n `91`; fx avg `-0.0037` n `6`; index avg `0.1468` n `25`; metal avg `0.0418` n `20`; unknown avg `-0.0363` n `763`
- 1h: commodity avg `-0.0828` n `12`; crypto_alt avg `0.4351` n `229`; crypto_major avg `0.1132` n `8`; equity avg `1.3931` n `91`; fx avg `-0.0229` n `6`; index avg `0.2922` n `25`; metal avg `0.1317` n `20`; unknown avg `0.311` n `763`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.1191` n `229`; crypto_major avg `-0.3302` n `8`; equity avg `0.6867` n `91`; fx avg `0.0525` n `6`; index avg `0.1965` n `25`; metal avg `0.0443` n `20`; unknown avg `-0.122` n `763`
- 24h: commodity avg `0.8113` n `12`; crypto_alt avg `-2.448` n `229`; crypto_major avg `-1.9512` n `8`; equity avg `-1.8125` n `91`; fx avg `-0.2012` n `6`; index avg `-0.207` n `25`; metal avg `-0.3986` n `20`; unknown avg `-0.2128` n `729`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
