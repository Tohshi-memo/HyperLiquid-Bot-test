# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T20:07:30.134732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `-0.031` n `237`; crypto_major avg `0.013` n `8`; equity avg `-0.0238` n `151`; fx avg `-0.021` n `6`; index avg `0.0006` n `26`; metal avg `-0.0167` n `20`; unknown avg `8.6116` n `1178`
- 1h: commodity avg `0.0326` n `13`; crypto_alt avg `-1.4723` n `237`; crypto_major avg `-0.9279` n `8`; equity avg `-0.2429` n `151`; fx avg `-0.048` n `6`; index avg `-0.0303` n `26`; metal avg `-0.0525` n `20`; unknown avg `9.2133` n `1178`
- 4h: commodity avg `0.0368` n `13`; crypto_alt avg `-1.8379` n `237`; crypto_major avg `-0.8082` n `8`; equity avg `-0.3203` n `151`; fx avg `-0.029` n `6`; index avg `-0.0435` n `26`; metal avg `-0.0329` n `20`; unknown avg `2.5749` n `1158`
- 24h: commodity avg `-0.0122` n `13`; crypto_alt avg `-5.2747` n `236`; crypto_major avg `-2.457` n `8`; equity avg `-1.3245` n `151`; fx avg `-0.0371` n `6`; index avg `-0.1823` n `26`; metal avg `-0.0994` n `20`; unknown avg `1.242` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.21`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0813`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
