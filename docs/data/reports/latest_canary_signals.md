# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T10:22:26.730671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0343` n `233`; crypto_major avg `0.0436` n `8`; equity avg `0.0351` n `134`; fx avg `0.0139` n `6`; index avg `0.007` n `26`; metal avg `0.0412` n `20`; unknown avg `-0.0485` n `798`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.6194` n `233`; crypto_major avg `-0.5485` n `8`; equity avg `-0.7123` n `134`; fx avg `0.0141` n `6`; index avg `-0.1219` n `26`; metal avg `-0.0092` n `20`; unknown avg `0.8201` n `796`
- 4h: commodity avg `0.1735` n `12`; crypto_alt avg `-0.3833` n `233`; crypto_major avg `-0.5609` n `8`; equity avg `-0.7086` n `134`; fx avg `0.0444` n `6`; index avg `-0.1578` n `26`; metal avg `-0.0269` n `20`; unknown avg `0.6415` n `790`
- 24h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.766` n `232`; crypto_major avg `0.2799` n `8`; equity avg `0.1729` n `134`; fx avg `-0.0783` n `6`; index avg `-0.1776` n `26`; metal avg `-0.097` n `20`; unknown avg `0.7631` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
