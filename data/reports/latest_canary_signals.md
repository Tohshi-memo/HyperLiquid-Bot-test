# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T03:07:33.483953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.548` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0011` n `233`; crypto_major avg `0.0616` n `8`; equity avg `-0.0447` n `136`; fx avg `-0.0008` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0148` n `20`; unknown avg `-0.0011` n `892`
- 1h: commodity avg `0.0919` n `12`; crypto_alt avg `0.6147` n `233`; crypto_major avg `0.8497` n `8`; equity avg `0.034` n `136`; fx avg `0.0152` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0806` n `20`; unknown avg `1.7536` n `892`
- 4h: commodity avg `0.0748` n `12`; crypto_alt avg `1.6788` n `233`; crypto_major avg `1.5353` n `8`; equity avg `0.0454` n `136`; fx avg `0.0291` n `6`; index avg `-0.0303` n `27`; metal avg `-0.0127` n `20`; unknown avg `18.956` n `768`
- 24h: commodity avg `0.7312` n `12`; crypto_alt avg `-0.5073` n `233`; crypto_major avg `-0.212` n `8`; equity avg `-1.3415` n `136`; fx avg `0.0736` n `6`; index avg `-0.2792` n `26`; metal avg `-0.116` n `20`; unknown avg `1.7896` n `682`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
