# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T17:07:47.247639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0889` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.0719` n `8`; equity avg `0.0039` n `114`; fx avg `0.0022` n `6`; index avg `-0.0072` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0019` n `792`
- 1h: commodity avg `0.1417` n `12`; crypto_alt avg `-0.0987` n `230`; crypto_major avg `-0.0472` n `8`; equity avg `0.0196` n `114`; fx avg `0.0086` n `6`; index avg `-0.0349` n `25`; metal avg `-0.0408` n `20`; unknown avg `0.0819` n `792`
- 4h: commodity avg `0.2167` n `12`; crypto_alt avg `0.0352` n `230`; crypto_major avg `0.374` n `8`; equity avg `0.7894` n `114`; fx avg `0.0113` n `6`; index avg `0.0597` n `25`; metal avg `0.1687` n `20`; unknown avg `0.0647` n `792`
- 24h: commodity avg `0.1348` n `12`; crypto_alt avg `-0.1925` n `230`; crypto_major avg `0.6327` n `8`; equity avg `1.6668` n `114`; fx avg `0.0149` n `6`; index avg `0.1734` n `25`; metal avg `0.2699` n `20`; unknown avg `0.0717` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
