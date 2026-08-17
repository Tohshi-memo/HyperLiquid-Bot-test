# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T00:52:28.624111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.0365` n `230`; crypto_major avg `0.0855` n `8`; equity avg `0.0634` n `114`; fx avg `-0.0267` n `6`; index avg `-0.0103` n `25`; metal avg `0.0577` n `20`; unknown avg `0.0346` n `792`
- 1h: commodity avg `-0.0565` n `12`; crypto_alt avg `-0.1021` n `230`; crypto_major avg `-0.0694` n `8`; equity avg `0.012` n `114`; fx avg `-0.0423` n `6`; index avg `-0.0329` n `25`; metal avg `0.1592` n `20`; unknown avg `-0.0677` n `792`
- 4h: commodity avg `-0.2098` n `12`; crypto_alt avg `-0.6408` n `230`; crypto_major avg `-0.4498` n `8`; equity avg `0.037` n `114`; fx avg `-0.0479` n `6`; index avg `0.0067` n `25`; metal avg `0.1432` n `20`; unknown avg `-0.1563` n `791`
- 24h: commodity avg `-0.1305` n `12`; crypto_alt avg `-0.7389` n `230`; crypto_major avg `-0.3974` n `8`; equity avg `0.3328` n `114`; fx avg `-0.0481` n `6`; index avg `0.0314` n `25`; metal avg `0.1668` n `20`; unknown avg `0.0642` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
