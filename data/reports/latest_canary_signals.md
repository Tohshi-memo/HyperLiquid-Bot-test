# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T17:52:39.423165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.0257` n `228`; crypto_major avg `0.0003` n `8`; equity avg `0.0211` n `88`; fx avg `0.0068` n `6`; index avg `0.0004` n `23`; metal avg `0.0769` n `20`; unknown avg `0.0455` n `765`
- 1h: commodity avg `-0.1482` n `12`; crypto_alt avg `0.0116` n `228`; crypto_major avg `0.0568` n `8`; equity avg `-0.0121` n `88`; fx avg `0.0034` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0234` n `20`; unknown avg `0.0403` n `765`
- 4h: commodity avg `-0.1794` n `12`; crypto_alt avg `0.2215` n `228`; crypto_major avg `0.1225` n `8`; equity avg `0.7085` n `88`; fx avg `0.0675` n `6`; index avg `0.1349` n `23`; metal avg `0.0462` n `20`; unknown avg `-0.3418` n `765`
- 24h: commodity avg `0.0087` n `12`; crypto_alt avg `-2.6642` n `228`; crypto_major avg `-2.6884` n `8`; equity avg `1.2509` n `88`; fx avg `0.1434` n `6`; index avg `0.3387` n `23`; metal avg `0.2516` n `20`; unknown avg `8.6102` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
