# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T23:52:31.608151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1158` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0573` n `233`; crypto_major avg `-0.0648` n `8`; equity avg `-0.0325` n `136`; fx avg `0.0067` n `6`; index avg `0.0087` n `27`; metal avg `-0.0241` n `20`; unknown avg `1.615` n `908`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.2891` n `233`; crypto_major avg `-0.4366` n `8`; equity avg `0.0147` n `136`; fx avg `0.0192` n `6`; index avg `0.0162` n `27`; metal avg `-0.0801` n `20`; unknown avg `0.4132` n `908`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.8317` n `233`; crypto_major avg `-1.1039` n `8`; equity avg `0.0272` n `136`; fx avg `0.0085` n `6`; index avg `0.0119` n `27`; metal avg `-0.0081` n `20`; unknown avg `2.3199` n `866`
- 24h: commodity avg `-0.087` n `12`; crypto_alt avg `1.193` n `233`; crypto_major avg `2.2315` n `8`; equity avg `0.0246` n `136`; fx avg `0.042` n `6`; index avg `-0.0496` n `27`; metal avg `-0.3503` n `20`; unknown avg `6.5621` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
