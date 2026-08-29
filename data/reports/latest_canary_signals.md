# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T18:40:19.146668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `0.0863` n `231`; crypto_major avg `0.1207` n `8`; equity avg `0.02` n `128`; fx avg `-0.0056` n `6`; index avg `0.0046` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.076` n `792`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `0.2488` n `231`; crypto_major avg `0.2679` n `8`; equity avg `0.0154` n `128`; fx avg `-0.0056` n `6`; index avg `-0.0059` n `26`; metal avg `0.003` n `20`; unknown avg `0.0766` n `792`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1616` n `231`; crypto_major avg `0.4698` n `8`; equity avg `0.028` n `128`; fx avg `-0.0043` n `6`; index avg `0.0028` n `26`; metal avg `0.0643` n `20`; unknown avg `0.0074` n `778`
- 24h: commodity avg `0.0506` n `12`; crypto_alt avg `1.5392` n `231`; crypto_major avg `1.5677` n `8`; equity avg `0.2455` n `128`; fx avg `-0.0445` n `6`; index avg `0.0253` n `26`; metal avg `0.1442` n `20`; unknown avg `0.2179` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2273`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
