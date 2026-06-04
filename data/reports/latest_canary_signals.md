# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T02:52:21.668030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.8681` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2481` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.2418` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.3721` n `228`; crypto_major avg `0.3363` n `8`; equity avg `0.1599` n `73`; fx avg `-0.0211` n `6`; index avg `0.0451` n `23`; metal avg `0.2191` n `18`; unknown avg `0.1782` n `420`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.2415` n `228`; crypto_major avg `1.1308` n `8`; equity avg `0.3821` n `73`; fx avg `-0.0236` n `6`; index avg `-0.0853` n `23`; metal avg `0.4299` n `18`; unknown avg `0.1648` n `420`
- 4h: commodity avg `-0.4237` n `12`; crypto_alt avg `-4.3405` n `228`; crypto_major avg `-2.3247` n `8`; equity avg `-0.0766` n `73`; fx avg `-0.0104` n `6`; index avg `-0.0829` n `23`; metal avg `0.5434` n `18`; unknown avg `-1.07` n `419`
- 24h: commodity avg `-0.0398` n `12`; crypto_alt avg `-2.6211` n `228`; crypto_major avg `-2.8776` n `8`; equity avg `-3.6173` n `73`; fx avg `-0.0289` n `6`; index avg `-1.1878` n `23`; metal avg `-1.4749` n `18`; unknown avg `0.3068` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
