# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T16:22:27.350169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.9582` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `-0.1509` n `230`; crypto_major avg `-0.1532` n `8`; equity avg `-0.2883` n `94`; fx avg `0.0167` n `6`; index avg `-0.052` n `25`; metal avg `-0.0641` n `20`; unknown avg `-0.0433` n `768`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `-0.4285` n `230`; crypto_major avg `-0.3763` n `8`; equity avg `-0.7772` n `94`; fx avg `0.0043` n `6`; index avg `-0.0931` n `25`; metal avg `-0.0711` n `20`; unknown avg `-0.0569` n `768`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.0299` n `230`; crypto_major avg `0.438` n `8`; equity avg `-2.5202` n `93`; fx avg `0.0957` n `6`; index avg `-0.4254` n `25`; metal avg `-0.0996` n `20`; unknown avg `0.273` n `768`
- 24h: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0406` n `230`; crypto_major avg `0.844` n `8`; equity avg `-1.9466` n `92`; fx avg `0.1579` n `6`; index avg `-0.3411` n `25`; metal avg `-0.2521` n `20`; unknown avg `0.2871` n `746`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
