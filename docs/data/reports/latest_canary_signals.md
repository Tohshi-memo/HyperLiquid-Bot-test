# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T06:22:24.753950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `13`; crypto_alt avg `0.1242` n `236`; crypto_major avg `0.1439` n `8`; equity avg `-0.1962` n `151`; fx avg `0.0009` n `6`; index avg `-0.049` n `26`; metal avg `-0.0132` n `20`; unknown avg `-0.1631` n `1136`
- 1h: commodity avg `-0.0767` n `13`; crypto_alt avg `-0.0118` n `236`; crypto_major avg `-0.0637` n `8`; equity avg `-0.5949` n `151`; fx avg `-0.0469` n `6`; index avg `-0.1186` n `26`; metal avg `-0.0772` n `20`; unknown avg `-0.157` n `1110`
- 4h: commodity avg `0.0376` n `13`; crypto_alt avg `0.3592` n `236`; crypto_major avg `0.1396` n `8`; equity avg `-0.0357` n `151`; fx avg `-0.0683` n `6`; index avg `-0.0416` n `26`; metal avg `0.0965` n `20`; unknown avg `0.0045` n `1102`
- 24h: commodity avg `-0.0672` n `13`; crypto_alt avg `4.5304` n `236`; crypto_major avg `2.4161` n `8`; equity avg `2.1478` n `151`; fx avg `-0.0211` n `6`; index avg `0.2737` n `26`; metal avg `0.4653` n `20`; unknown avg `25.8337` n `904`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0978`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0956`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0641`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
