# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T17:07:31.307800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0776` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1111` n `12`; crypto_alt avg `0.0203` n `233`; crypto_major avg `-0.0348` n `8`; equity avg `-0.0486` n `134`; fx avg `0.0145` n `6`; index avg `-0.003` n `26`; metal avg `0.1201` n `20`; unknown avg `8.3552` n `795`
- 1h: commodity avg `-0.2655` n `12`; crypto_alt avg `0.3949` n `233`; crypto_major avg `0.0969` n `8`; equity avg `-0.0127` n `134`; fx avg `0.0383` n `6`; index avg `0.0106` n `26`; metal avg `0.1946` n `20`; unknown avg `2.8914` n `789`
- 4h: commodity avg `-0.125` n `12`; crypto_alt avg `-1.0261` n `233`; crypto_major avg `-1.104` n `8`; equity avg `0.1125` n `134`; fx avg `0.0467` n `6`; index avg `-0.0264` n `26`; metal avg `0.3344` n `20`; unknown avg `6.7957` n `767`
- 24h: commodity avg `0.3646` n `12`; crypto_alt avg `-1.214` n `233`; crypto_major avg `-0.568` n `8`; equity avg `-0.6941` n `134`; fx avg `-0.0703` n `6`; index avg `-0.2331` n `26`; metal avg `0.452` n `20`; unknown avg `4.8485` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
