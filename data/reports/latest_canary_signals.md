# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T10:16:08.842072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.1719` n `230`; crypto_major avg `-0.1448` n `8`; equity avg `-0.011` n `113`; fx avg `-0.001` n `6`; index avg `0.0035` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0266` n `785`
- 1h: commodity avg `-0.0795` n `12`; crypto_alt avg `-0.1789` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.0492` n `113`; fx avg `-0.0044` n `6`; index avg `0.0125` n `25`; metal avg `0.0288` n `20`; unknown avg `-0.0933` n `785`
- 4h: commodity avg `0.1886` n `12`; crypto_alt avg `-0.2978` n `230`; crypto_major avg `0.1489` n `8`; equity avg `-0.188` n `113`; fx avg `-0.0051` n `6`; index avg `-0.0043` n `25`; metal avg `0.1434` n `20`; unknown avg `-0.0362` n `785`
- 24h: commodity avg `1.1173` n `12`; crypto_alt avg `-1.2384` n `230`; crypto_major avg `-0.644` n `8`; equity avg `-1.3959` n `113`; fx avg `0.0123` n `6`; index avg `-0.027` n `25`; metal avg `0.3367` n `20`; unknown avg `0.1114` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
