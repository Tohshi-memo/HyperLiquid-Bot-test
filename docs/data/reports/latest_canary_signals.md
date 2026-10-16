# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T05:52:28.288305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `0.1758` n `236`; crypto_major avg `0.1378` n `8`; equity avg `0.1102` n `151`; fx avg `-0.019` n `6`; index avg `0.0182` n `26`; metal avg `0.0062` n `20`; unknown avg `-0.1369` n `1136`
- 1h: commodity avg `-0.0591` n `13`; crypto_alt avg `0.3901` n `236`; crypto_major avg `0.3413` n `8`; equity avg `-0.1841` n `151`; fx avg `-0.0843` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0267` n `20`; unknown avg `4.138` n `1134`
- 4h: commodity avg `-0.0592` n `13`; crypto_alt avg `0.5661` n `236`; crypto_major avg `0.3796` n `8`; equity avg `0.5851` n `151`; fx avg `-0.0667` n `6`; index avg `0.0872` n `26`; metal avg `0.2156` n `20`; unknown avg `0.2511` n `1124`
- 24h: commodity avg `-0.0641` n `13`; crypto_alt avg `4.8852` n `236`; crypto_major avg `2.7677` n `8`; equity avg `2.7693` n `151`; fx avg `-0.0456` n `6`; index avg `0.4629` n `26`; metal avg `0.4747` n `20`; unknown avg `26.3084` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1033`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0612`, n `666`, weak_sample_signal
