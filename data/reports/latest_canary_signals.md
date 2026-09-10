# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T08:07:32.278883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0857` n `233`; crypto_major avg `0.0005` n `8`; equity avg `-0.0497` n `134`; fx avg `0.0033` n `6`; index avg `-0.0011` n `26`; metal avg `-0.028` n `20`; unknown avg `1.786` n `795`
- 1h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.462` n `233`; crypto_major avg `-0.0691` n `8`; equity avg `-0.1314` n `134`; fx avg `0.0177` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0589` n `20`; unknown avg `1.2431` n `795`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.7394` n `233`; crypto_major avg `-0.5543` n `8`; equity avg `-0.0447` n `134`; fx avg `0.0562` n `6`; index avg `0.0284` n `26`; metal avg `-0.1018` n `20`; unknown avg `1.6118` n `765`
- 24h: commodity avg `-0.0645` n `12`; crypto_alt avg `-4.772` n `233`; crypto_major avg `-3.2924` n `8`; equity avg `-1.3526` n `134`; fx avg `0.0775` n `6`; index avg `-0.1553` n `26`; metal avg `0.0739` n `20`; unknown avg `0.4836` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
