# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T01:37:29.978727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `13`; crypto_alt avg `-0.2102` n `235`; crypto_major avg `-0.1623` n `8`; equity avg `-0.0766` n `151`; fx avg `-0.0038` n `6`; index avg `0.0105` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.1459` n `1135`
- 1h: commodity avg `0.0564` n `13`; crypto_alt avg `-0.6402` n `235`; crypto_major avg `-0.4563` n `8`; equity avg `-0.4372` n `151`; fx avg `-0.0003` n `6`; index avg `-0.0636` n `26`; metal avg `-0.0828` n `20`; unknown avg `0.4155` n `1133`
- 4h: commodity avg `0.1495` n `13`; crypto_alt avg `-0.2567` n `235`; crypto_major avg `-0.074` n `8`; equity avg `-0.1325` n `151`; fx avg `0.0349` n `6`; index avg `-0.0271` n `26`; metal avg `-0.1438` n `20`; unknown avg `0.2872` n `1071`
- 24h: commodity avg `0.9808` n `13`; crypto_alt avg `1.4379` n `235`; crypto_major avg `1.3803` n `8`; equity avg `0.6978` n `151`; fx avg `0.1299` n `6`; index avg `0.1102` n `26`; metal avg `-0.2412` n `20`; unknown avg `1.2301` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1565`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1431`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1103`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0953`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
