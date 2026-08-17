# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T00:22:29.846364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.1615` n `230`; crypto_major avg `-0.1188` n `8`; equity avg `-0.0528` n `114`; fx avg `-0.0189` n `6`; index avg `-0.0086` n `25`; metal avg `0.0464` n `20`; unknown avg `-0.0509` n `792`
- 1h: commodity avg `-0.084` n `12`; crypto_alt avg `-0.1191` n `230`; crypto_major avg `-0.0975` n `8`; equity avg `-0.0053` n `114`; fx avg `-0.0175` n `6`; index avg `0.0098` n `25`; metal avg `0.0431` n `20`; unknown avg `-0.1373` n `791`
- 4h: commodity avg `-0.1917` n `12`; crypto_alt avg `-0.8829` n `230`; crypto_major avg `-0.6821` n `8`; equity avg `-0.0163` n `114`; fx avg `-0.0238` n `6`; index avg `0.0203` n `25`; metal avg `0.0682` n `20`; unknown avg `0.1032` n `791`
- 24h: commodity avg `-0.1327` n `12`; crypto_alt avg `-0.7764` n `230`; crypto_major avg `-0.451` n `8`; equity avg `0.2514` n `114`; fx avg `-0.0284` n `6`; index avg `0.0518` n `25`; metal avg `0.1006` n `20`; unknown avg `0.0034` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
