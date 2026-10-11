# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T17:22:30.865409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `0.1352` n `235`; crypto_major avg `0.2263` n `8`; equity avg `0.0145` n `150`; fx avg `-0.0089` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0015` n `20`; unknown avg `7.7574` n `1126`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `0.0997` n `235`; crypto_major avg `0.2468` n `8`; equity avg `0.0945` n `150`; fx avg `0.0009` n `6`; index avg `0.0147` n `26`; metal avg `0.0429` n `20`; unknown avg `0.2208` n `1124`
- 4h: commodity avg `-0.0634` n `13`; crypto_alt avg `2.0589` n `235`; crypto_major avg `1.5363` n `8`; equity avg `0.2538` n `150`; fx avg `-0.0151` n `6`; index avg `0.0445` n `26`; metal avg `0.0634` n `20`; unknown avg `21.9342` n `1102`
- 24h: commodity avg `0.2218` n `13`; crypto_alt avg `2.411` n `235`; crypto_major avg `1.2091` n `8`; equity avg `0.3447` n `150`; fx avg `0.0171` n `6`; index avg `0.0348` n `26`; metal avg `0.0911` n `20`; unknown avg `0.8509` n `917`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
