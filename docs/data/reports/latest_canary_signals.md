# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T03:52:28.703801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `-0.1621` n `8`; equity avg `-0.0483` n `94`; fx avg `0.0037` n `6`; index avg `0.0081` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.1189` n `768`
- 1h: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.197` n `230`; crypto_major avg `-0.1803` n `8`; equity avg `-0.0423` n `94`; fx avg `-0.0077` n `6`; index avg `-0.0061` n `25`; metal avg `0.1082` n `20`; unknown avg `-0.3933` n `768`
- 4h: commodity avg `-0.1326` n `12`; crypto_alt avg `-0.0257` n `230`; crypto_major avg `-0.3223` n `8`; equity avg `-0.2287` n `94`; fx avg `-0.0333` n `6`; index avg `-0.0937` n `25`; metal avg `-0.1183` n `20`; unknown avg `-0.6232` n `766`
- 24h: commodity avg `-0.0895` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `-0.1387` n `8`; equity avg `-2.3312` n `93`; fx avg `0.1082` n `6`; index avg `-0.4757` n `25`; metal avg `0.0553` n `20`; unknown avg `-0.1641` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
