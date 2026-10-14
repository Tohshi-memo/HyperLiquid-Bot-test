# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T05:07:23.739651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.402` n `235`; crypto_major avg `-0.2679` n `8`; equity avg `-0.2411` n `151`; fx avg `-0.0132` n `6`; index avg `-0.0293` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.1914` n `1133`
- 1h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.0355` n `235`; crypto_major avg `-0.0669` n `8`; equity avg `-0.3396` n `151`; fx avg `-0.0197` n `6`; index avg `-0.0317` n `26`; metal avg `0.0527` n `20`; unknown avg `-0.0334` n `1133`
- 4h: commodity avg `-0.1742` n `13`; crypto_alt avg `0.2019` n `235`; crypto_major avg `0.1415` n `8`; equity avg `-0.1582` n `151`; fx avg `-0.0503` n `6`; index avg `0.0353` n `26`; metal avg `0.1158` n `20`; unknown avg `-0.2767` n `1127`
- 24h: commodity avg `1.0313` n `13`; crypto_alt avg `-0.6114` n `235`; crypto_major avg `-0.2055` n `8`; equity avg `0.3599` n `151`; fx avg `0.0312` n `6`; index avg `0.1461` n `26`; metal avg `-0.3197` n `20`; unknown avg `1.1267` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1363`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `666`, weak_sample_signal
