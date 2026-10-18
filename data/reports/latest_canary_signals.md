# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T08:52:30.828668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `0.0376` n `237`; crypto_major avg `0.0389` n `8`; equity avg `0.0385` n `151`; fx avg `0.003` n `6`; index avg `0.0075` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.8268` n `1153`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `-0.1666` n `237`; crypto_major avg `0.0012` n `8`; equity avg `0.0983` n `151`; fx avg `-0.0023` n `6`; index avg `0.0152` n `26`; metal avg `0.0009` n `20`; unknown avg `0.5832` n `1135`
- 4h: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.6896` n `237`; crypto_major avg `-0.348` n `8`; equity avg `0.1456` n `151`; fx avg `0.0057` n `6`; index avg `0.0346` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.1232` n `1119`
- 24h: commodity avg `0.0469` n `13`; crypto_alt avg `-2.8428` n `236`; crypto_major avg `-1.0057` n `8`; equity avg `-0.7337` n `151`; fx avg `-0.0273` n `6`; index avg `-0.078` n `26`; metal avg `-0.074` n `20`; unknown avg `4.4197` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1792`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
