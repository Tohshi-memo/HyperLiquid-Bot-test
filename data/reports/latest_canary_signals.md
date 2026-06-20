# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T00:37:28.521711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.3781` n `228`; crypto_major avg `0.2438` n `8`; equity avg `0.0566` n `78`; fx avg `0.0059` n `6`; index avg `0.0074` n `23`; metal avg `0.0138` n `18`; unknown avg `-0.0616` n `687`
- 1h: commodity avg `-0.0311` n `12`; crypto_alt avg `0.5717` n `228`; crypto_major avg `0.3028` n `8`; equity avg `0.0705` n `78`; fx avg `0.035` n `6`; index avg `0.0237` n `23`; metal avg `0.0016` n `18`; unknown avg `-0.1786` n `679`
- 4h: commodity avg `-0.0208` n `12`; crypto_alt avg `1.0255` n `228`; crypto_major avg `0.644` n `8`; equity avg `0.3317` n `78`; fx avg `0.0652` n `6`; index avg `0.0619` n `23`; metal avg `0.0726` n `18`; unknown avg `-0.2245` n `679`
- 24h: commodity avg `0.2808` n `12`; crypto_alt avg `-2.9164` n `228`; crypto_major avg `-4.1175` n `8`; equity avg `0.9996` n `78`; fx avg `-0.0789` n `6`; index avg `0.2839` n `23`; metal avg `-4.0921` n `18`; unknown avg `-0.458` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
