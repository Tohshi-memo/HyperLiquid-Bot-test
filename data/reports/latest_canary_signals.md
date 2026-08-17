# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T23:53:08.730237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0755` n `230`; crypto_major avg `0.0514` n `8`; equity avg `-0.0519` n `114`; fx avg `0.0082` n `6`; index avg `-0.0232` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0638` n `793`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.1628` n `230`; crypto_major avg `0.3174` n `8`; equity avg `-0.093` n `114`; fx avg `-0.0163` n `6`; index avg `-0.0453` n `25`; metal avg `0.0522` n `20`; unknown avg `-0.1554` n `793`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `-0.1179` n `230`; crypto_major avg `0.3387` n `8`; equity avg `0.0118` n `114`; fx avg `-0.0029` n `6`; index avg `-0.0171` n `25`; metal avg `0.0251` n `20`; unknown avg `-0.2527` n `792`
- 24h: commodity avg `0.5579` n `12`; crypto_alt avg `0.4953` n `230`; crypto_major avg `1.6488` n `8`; equity avg `1.081` n `114`; fx avg `0.0117` n `6`; index avg `0.008` n `25`; metal avg `0.2604` n `20`; unknown avg `0.38` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
