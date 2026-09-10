# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T02:07:27.161209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.29` n `233`; crypto_major avg `0.2931` n `8`; equity avg `0.0461` n `134`; fx avg `-0.0389` n `6`; index avg `0.0171` n `26`; metal avg `0.0708` n `20`; unknown avg `0.1015` n `795`
- 1h: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.6987` n `233`; crypto_major avg `-0.367` n `8`; equity avg `-0.1264` n `134`; fx avg `-0.0065` n `6`; index avg `0.0229` n `26`; metal avg `0.0109` n `20`; unknown avg `0.9171` n `795`
- 4h: commodity avg `-0.2041` n `12`; crypto_alt avg `-0.9746` n `233`; crypto_major avg `-0.1465` n `8`; equity avg `-0.4431` n `134`; fx avg `-0.0194` n `6`; index avg `-0.0278` n `26`; metal avg `0.0279` n `20`; unknown avg `-0.0203` n `757`
- 24h: commodity avg `-0.0229` n `12`; crypto_alt avg `-3.6291` n `233`; crypto_major avg `-2.4302` n `8`; equity avg `-1.4209` n `134`; fx avg `-0.0173` n `6`; index avg `-0.2543` n `26`; metal avg `0.4756` n `20`; unknown avg `0.9687` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
