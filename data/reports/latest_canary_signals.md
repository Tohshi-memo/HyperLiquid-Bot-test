# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T11:07:25.276173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.136` n `230`; crypto_major avg `0.1137` n `8`; equity avg `0.1814` n `108`; fx avg `-0.0033` n `6`; index avg `0.0265` n `25`; metal avg `0.083` n `20`; unknown avg `0.0291` n `782`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.0352` n `230`; crypto_major avg `-0.005` n `8`; equity avg `0.0702` n `108`; fx avg `-0.014` n `6`; index avg `0.0218` n `25`; metal avg `0.0741` n `20`; unknown avg `0.0406` n `781`
- 4h: commodity avg `0.1867` n `12`; crypto_alt avg `-0.1377` n `230`; crypto_major avg `-0.1604` n `8`; equity avg `-0.7569` n `108`; fx avg `0.0068` n `6`; index avg `-0.0985` n `25`; metal avg `-0.183` n `20`; unknown avg `0.6445` n `781`
- 24h: commodity avg `-0.9707` n `12`; crypto_alt avg `0.6517` n `230`; crypto_major avg `0.5051` n `8`; equity avg `2.0081` n `108`; fx avg `-0.0042` n `6`; index avg `0.5805` n `25`; metal avg `1.0678` n `20`; unknown avg `0.1435` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
