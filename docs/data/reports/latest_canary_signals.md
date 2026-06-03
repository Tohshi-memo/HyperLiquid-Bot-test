# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T16:52:25.579358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0821` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1385` n `12`; crypto_alt avg `0.1932` n `228`; crypto_major avg `0.1556` n `8`; equity avg `0.0807` n `73`; fx avg `-0.0016` n `6`; index avg `-0.061` n `23`; metal avg `-0.0454` n `18`; unknown avg `0.9183` n `419`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.8615` n `228`; crypto_major avg `-0.5938` n `8`; equity avg `-0.3539` n `73`; fx avg `-0.0127` n `6`; index avg `-0.1106` n `23`; metal avg `-0.1896` n `18`; unknown avg `-0.2992` n `419`
- 4h: commodity avg `-0.17` n `12`; crypto_alt avg `-1.0509` n `228`; crypto_major avg `-1.72` n `8`; equity avg `-2.3122` n `73`; fx avg `0.0045` n `6`; index avg `-0.6379` n `23`; metal avg `-1.135` n `18`; unknown avg `0.8238` n `419`
- 24h: commodity avg `0.936` n `12`; crypto_alt avg `0.0944` n `228`; crypto_major avg `-2.8305` n `8`; equity avg `-2.3488` n `72`; fx avg `0.0219` n `6`; index avg `-0.3253` n `23`; metal avg `-2.1014` n `18`; unknown avg `0.9026` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
