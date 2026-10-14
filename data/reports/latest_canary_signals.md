# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T13:52:29.916961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.1718` n `235`; crypto_major avg `-0.2274` n `8`; equity avg `-0.0037` n `151`; fx avg `0.0005` n `6`; index avg `-0.0034` n `26`; metal avg `-0.1554` n `20`; unknown avg `0.0167` n `1134`
- 1h: commodity avg `0.0361` n `13`; crypto_alt avg `-0.185` n `235`; crypto_major avg `-0.2233` n `8`; equity avg `-0.5664` n `151`; fx avg `-0.012` n `6`; index avg `-0.0307` n `26`; metal avg `-0.2663` n `20`; unknown avg `11.772` n `1132`
- 4h: commodity avg `-0.1294` n `13`; crypto_alt avg `-0.9274` n `235`; crypto_major avg `-0.6463` n `8`; equity avg `-1.6902` n `151`; fx avg `-0.0696` n `6`; index avg `-0.2329` n `26`; metal avg `-0.5187` n `20`; unknown avg `2.6999` n `1125`
- 24h: commodity avg `0.4176` n `13`; crypto_alt avg `-1.3032` n `235`; crypto_major avg `-0.7472` n `8`; equity avg `-1.6654` n `151`; fx avg `-0.116` n `6`; index avg `-0.2178` n `26`; metal avg `-0.7409` n `20`; unknown avg `1262.7785` n `981`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1369`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0697`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0556`, n `666`, weak_sample_signal
