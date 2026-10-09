# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T19:52:29.200427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.2406` n `235`; crypto_major avg `-0.2202` n `8`; equity avg `-0.015` n `150`; fx avg `-0.0041` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0271` n `20`; unknown avg `6.1381` n `1092`
- 1h: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.6896` n `235`; crypto_major avg `-0.4828` n `8`; equity avg `-0.1597` n `150`; fx avg `-0.0104` n `6`; index avg `-0.036` n `26`; metal avg `-0.0619` n `20`; unknown avg `10.8448` n `1090`
- 4h: commodity avg `-0.3805` n `13`; crypto_alt avg `-0.707` n `235`; crypto_major avg `-0.6748` n `8`; equity avg `0.0454` n `150`; fx avg `-0.0131` n `6`; index avg `0.0153` n `26`; metal avg `-0.0386` n `20`; unknown avg `11.0913` n `1076`
- 24h: commodity avg `-0.1652` n `13`; crypto_alt avg `1.2184` n `235`; crypto_major avg `0.1921` n `8`; equity avg `1.0501` n `150`; fx avg `0.0018` n `6`; index avg `0.1706` n `26`; metal avg `0.5912` n `20`; unknown avg `5.1583` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
