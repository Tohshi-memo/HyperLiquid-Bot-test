# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T11:37:34.166535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `0.0624` n `239`; crypto_major avg `0.1239` n `8`; equity avg `0.0506` n `168`; fx avg `0.0017` n `6`; index avg `0.0006` n `27`; metal avg `-0.0004` n `20`; unknown avg `3.5788` n `1269`
- 1h: commodity avg `-0.0263` n `13`; crypto_alt avg `-0.0278` n `239`; crypto_major avg `0.1009` n `8`; equity avg `-0.0306` n `168`; fx avg `0.0059` n `6`; index avg `-0.0117` n `27`; metal avg `0.0106` n `20`; unknown avg `3.9139` n `1263`
- 4h: commodity avg `-0.0539` n `13`; crypto_alt avg `-0.568` n `239`; crypto_major avg `-0.6066` n `8`; equity avg `-0.1603` n `168`; fx avg `0.006` n `6`; index avg `-0.0209` n `27`; metal avg `0.0088` n `20`; unknown avg `3.4101` n `1213`
- 24h: commodity avg `-0.6102` n `13`; crypto_alt avg `-3.3466` n `239`; crypto_major avg `-3.3653` n `8`; equity avg `-0.2092` n `168`; fx avg `-0.0676` n `6`; index avg `0.0172` n `27`; metal avg `-0.224` n `20`; unknown avg `191.2892` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
