# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T03:22:31.145832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4729` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `0.4915` n `228`; crypto_major avg `0.3356` n `8`; equity avg `-0.0508` n `86`; fx avg `0.0145` n `6`; index avg `-0.0045` n `23`; metal avg `0.0597` n `20`; unknown avg `0.2023` n `765`
- 1h: commodity avg `-0.1315` n `12`; crypto_alt avg `0.7093` n `228`; crypto_major avg `0.5763` n `8`; equity avg `-0.6486` n `86`; fx avg `0.0001` n `6`; index avg `-0.1758` n `23`; metal avg `-0.1478` n `20`; unknown avg `22.1932` n `765`
- 4h: commodity avg `-0.1696` n `12`; crypto_alt avg `-1.7189` n `228`; crypto_major avg `-2.0292` n `8`; equity avg `-2.597` n `86`; fx avg `0.038` n `6`; index avg `-0.5563` n `23`; metal avg `-0.6203` n `20`; unknown avg `-0.4676` n `749`
- 24h: commodity avg `0.3407` n `12`; crypto_alt avg `-2.6162` n `228`; crypto_major avg `-2.7576` n `8`; equity avg `-4.2648` n `86`; fx avg `0.062` n `6`; index avg `-0.6751` n `23`; metal avg `0.0064` n `20`; unknown avg `0.2611` n `717`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
