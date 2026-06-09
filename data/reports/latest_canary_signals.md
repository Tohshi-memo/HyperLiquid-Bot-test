# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T00:52:24.759485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3821` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0989` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1001` n `12`; crypto_alt avg `-0.3244` n `228`; crypto_major avg `-0.3002` n `8`; equity avg `-0.0209` n `74`; fx avg `0.009` n `6`; index avg `-0.0228` n `23`; metal avg `-0.0071` n `18`; unknown avg `-0.0046` n `517`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-1.6659` n `228`; crypto_major avg `-1.3795` n `8`; equity avg `-0.5099` n `74`; fx avg `-0.0601` n `6`; index avg `-0.2806` n `23`; metal avg `-0.1713` n `18`; unknown avg `-0.1188` n `517`
- 4h: commodity avg `-0.1189` n `12`; crypto_alt avg `-2.7565` n `228`; crypto_major avg `-1.7528` n `8`; equity avg `-0.5672` n `74`; fx avg `-0.0491` n `6`; index avg `-0.3707` n `23`; metal avg `-0.4333` n `18`; unknown avg `-0.7027` n `517`
- 24h: commodity avg `-0.5387` n `12`; crypto_alt avg `-2.2752` n `228`; crypto_major avg `-1.4715` n `8`; equity avg `0.451` n `74`; fx avg `-0.2908` n `6`; index avg `0.2122` n `23`; metal avg `-0.7612` n `18`; unknown avg `-3.4308` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
