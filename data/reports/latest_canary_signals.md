# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T02:03:51.457307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.057` n `8`; equity avg `-0.0084` n `114`; fx avg `0.0186` n `6`; index avg `0.0134` n `25`; metal avg `-0.0279` n `20`; unknown avg `0.127` n `793`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `-0.4407` n `230`; crypto_major avg `-0.3121` n `8`; equity avg `-0.8965` n `114`; fx avg `0.0134` n `6`; index avg `-0.1092` n `25`; metal avg `-0.2704` n `20`; unknown avg `0.5014` n `793`
- 4h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.6105` n `230`; crypto_major avg `-0.2014` n `8`; equity avg `-0.9338` n `114`; fx avg `-0.0655` n `6`; index avg `-0.1334` n `25`; metal avg `-0.1463` n `20`; unknown avg `-0.0983` n `792`
- 24h: commodity avg `0.5179` n `12`; crypto_alt avg `-0.3285` n `230`; crypto_major avg `0.5873` n `8`; equity avg `0.1867` n `114`; fx avg `0.0169` n `6`; index avg `-0.0632` n `25`; metal avg `-0.1429` n `20`; unknown avg `0.2414` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
