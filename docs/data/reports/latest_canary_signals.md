# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T20:07:27.189834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1291` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1032` n `12`; crypto_alt avg `-0.331` n `228`; crypto_major avg `-0.1567` n `8`; equity avg `0.0432` n `74`; fx avg `-0.0008` n `6`; index avg `0.0429` n `23`; metal avg `-0.0023` n `18`; unknown avg `-0.0261` n `515`
- 1h: commodity avg `0.1094` n `12`; crypto_alt avg `-0.7473` n `228`; crypto_major avg `-0.6467` n `8`; equity avg `0.0859` n `74`; fx avg `-0.0299` n `6`; index avg `-0.0259` n `23`; metal avg `-0.0137` n `18`; unknown avg `-0.2407` n `515`
- 4h: commodity avg `0.2052` n `12`; crypto_alt avg `-1.0818` n `228`; crypto_major avg `-1.2289` n `8`; equity avg `0.1737` n `74`; fx avg `0.067` n `6`; index avg `-0.0998` n `23`; metal avg `0.065` n `18`; unknown avg `0.2051` n `515`
- 24h: commodity avg `0.5561` n `12`; crypto_alt avg `-0.966` n `228`; crypto_major avg `-0.9007` n `8`; equity avg `-0.5817` n `74`; fx avg `0.0645` n `6`; index avg `0.1016` n `23`; metal avg `-0.236` n `18`; unknown avg `0.5386` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
