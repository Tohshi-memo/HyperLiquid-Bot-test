# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T18:48:35.204562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.84` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `-0.0837` n `230`; crypto_major avg `-0.1311` n `8`; equity avg `-0.2124` n `94`; fx avg `-0.0013` n `6`; index avg `-0.0425` n `25`; metal avg `-0.0324` n `20`; unknown avg `0.0182` n `768`
- 1h: commodity avg `0.1459` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `0.0066` n `8`; equity avg `-0.0402` n `94`; fx avg `-0.0005` n `6`; index avg `-0.0043` n `25`; metal avg `0.1798` n `20`; unknown avg `-0.0383` n `768`
- 4h: commodity avg `0.254` n `12`; crypto_alt avg `-0.2978` n `230`; crypto_major avg `-0.4886` n `8`; equity avg `-0.0574` n `94`; fx avg `0.0547` n `6`; index avg `0.0868` n `25`; metal avg `0.1789` n `20`; unknown avg `-0.0052` n `768`
- 24h: commodity avg `0.0827` n `12`; crypto_alt avg `0.7042` n `230`; crypto_major avg `1.0912` n `8`; equity avg `-0.4332` n `93`; fx avg `0.2229` n `6`; index avg `-0.1756` n `25`; metal avg `0.2198` n `20`; unknown avg `0.3309` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
