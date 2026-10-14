# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T16:37:33.121140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1139` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `0.5378` n `235`; crypto_major avg `0.3387` n `8`; equity avg `0.1304` n `151`; fx avg `0.0119` n `6`; index avg `0.0122` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.6812` n `1137`
- 1h: commodity avg `0.1066` n `13`; crypto_alt avg `0.044` n `235`; crypto_major avg `-0.23` n `8`; equity avg `-0.4399` n `151`; fx avg `0.0026` n `6`; index avg `-0.0832` n `26`; metal avg `-0.0694` n `20`; unknown avg `0.7807` n `1129`
- 4h: commodity avg `-0.0465` n `13`; crypto_alt avg `-1.337` n `235`; crypto_major avg `-1.3764` n `8`; equity avg `-2.1239` n `151`; fx avg `-0.0807` n `6`; index avg `-0.2625` n `26`; metal avg `-0.5531` n `20`; unknown avg `0.4082` n `1102`
- 24h: commodity avg `0.0357` n `13`; crypto_alt avg `-2.4423` n `235`; crypto_major avg `-2.1001` n `8`; equity avg `-3.5307` n `151`; fx avg `-0.1463` n `6`; index avg `-0.4778` n `26`; metal avg `-0.8339` n `20`; unknown avg `1261.7028` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0677`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
