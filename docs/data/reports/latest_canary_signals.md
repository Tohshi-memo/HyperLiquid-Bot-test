# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T03:37:26.113561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `-0.4369` n `239`; crypto_major avg `-0.4517` n `8`; equity avg `-0.294` n `162`; fx avg `-0.0037` n `6`; index avg `-0.0487` n `27`; metal avg `-0.0584` n `20`; unknown avg `0.3939` n `1263`
- 1h: commodity avg `-0.0378` n `13`; crypto_alt avg `-0.6977` n `239`; crypto_major avg `-0.6839` n `8`; equity avg `-0.5749` n `162`; fx avg `-0.0087` n `6`; index avg `-0.0851` n `27`; metal avg `-0.0909` n `20`; unknown avg `0.2858` n `1259`
- 4h: commodity avg `-0.0969` n `13`; crypto_alt avg `-0.717` n `239`; crypto_major avg `-1.1078` n `8`; equity avg `-1.3829` n `162`; fx avg `-0.0215` n `6`; index avg `-0.253` n `27`; metal avg `-0.4047` n `20`; unknown avg `1.6567` n `1239`
- 24h: commodity avg `-0.4297` n `13`; crypto_alt avg `-0.3666` n `239`; crypto_major avg `-0.3654` n `8`; equity avg `0.1027` n `162`; fx avg `-0.0105` n `6`; index avg `0.0015` n `27`; metal avg `0.0832` n `20`; unknown avg `0.9756` n `1123`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
