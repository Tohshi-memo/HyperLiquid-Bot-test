# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T02:07:29.061615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5689` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3908` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.079` n `228`; crypto_major avg `0.0381` n `8`; equity avg `0.0652` n `74`; fx avg `-0.0115` n `6`; index avg `-0.0491` n `23`; metal avg `-0.0831` n `18`; unknown avg `0.0621` n `517`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `0.4204` n `228`; crypto_major avg `0.3484` n `8`; equity avg `0.5188` n `74`; fx avg `-0.0203` n `6`; index avg `0.2739` n `23`; metal avg `0.1257` n `18`; unknown avg `0.1323` n `517`
- 4h: commodity avg `-0.1281` n `12`; crypto_alt avg `-2.0262` n `228`; crypto_major avg `-1.5432` n `8`; equity avg `0.0257` n `74`; fx avg `-0.0439` n `6`; index avg `-0.1524` n `23`; metal avg `-0.0618` n `18`; unknown avg `-0.4106` n `517`
- 24h: commodity avg `-0.8662` n `12`; crypto_alt avg `-0.4461` n `228`; crypto_major avg `-0.0539` n `8`; equity avg `1.4871` n `74`; fx avg `-0.3259` n `6`; index avg `0.8802` n `23`; metal avg `-0.0003` n `18`; unknown avg `-2.7881` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
