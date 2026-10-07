# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T11:07:27.794166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.098` n `13`; crypto_alt avg `-0.0509` n `235`; crypto_major avg `0.0116` n `8`; equity avg `-0.2072` n `150`; fx avg `-0.0023` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0176` n `20`; unknown avg `0.3537` n `1074`
- 1h: commodity avg `0.1802` n `13`; crypto_alt avg `0.07` n `235`; crypto_major avg `0.1356` n `8`; equity avg `-0.3146` n `150`; fx avg `0.0028` n `6`; index avg `-0.0715` n `26`; metal avg `-0.034` n `20`; unknown avg `1.5907` n `1074`
- 4h: commodity avg `0.2737` n `13`; crypto_alt avg `-1.3564` n `235`; crypto_major avg `-0.9531` n `8`; equity avg `-1.0206` n `150`; fx avg `-0.1069` n `6`; index avg `-0.1545` n `26`; metal avg `-0.238` n `20`; unknown avg `1.6197` n `1058`
- 24h: commodity avg `1.4083` n `13`; crypto_alt avg `-4.8595` n `235`; crypto_major avg `-3.2519` n `8`; equity avg `-1.3931` n `150`; fx avg `-0.1029` n `6`; index avg `-0.2903` n `26`; metal avg `-0.4385` n `20`; unknown avg `815.5992` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
