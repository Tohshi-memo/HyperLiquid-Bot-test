# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T02:22:27.330637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2474` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0414` n `12`; crypto_alt avg `0.3041` n `231`; crypto_major avg `0.1434` n `8`; equity avg `-0.0592` n `128`; fx avg `-0.0066` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0685` n `20`; unknown avg `0.0081` n `793`
- 1h: commodity avg `0.1114` n `12`; crypto_alt avg `0.1732` n `231`; crypto_major avg `0.0667` n `8`; equity avg `0.1046` n `128`; fx avg `-0.0248` n `6`; index avg `0.0381` n `26`; metal avg `-0.1266` n `20`; unknown avg `-0.1755` n `779`
- 4h: commodity avg `0.0411` n `12`; crypto_alt avg `-1.3058` n `231`; crypto_major avg `-1.461` n `8`; equity avg `-1.0372` n `128`; fx avg `-0.0357` n `6`; index avg `-0.2136` n `26`; metal avg `-0.3546` n `20`; unknown avg `0.7369` n `779`
- 24h: commodity avg `0.4013` n `12`; crypto_alt avg `-0.3883` n `231`; crypto_major avg `-1.9895` n `8`; equity avg `-1.2273` n `128`; fx avg `-0.029` n `6`; index avg `-0.2684` n `26`; metal avg `-0.4251` n `20`; unknown avg `-0.3745` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
