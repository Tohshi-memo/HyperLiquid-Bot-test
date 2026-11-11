# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T22:52:29.775638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.4025` n `239`; crypto_major avg `-0.3826` n `8`; equity avg `-0.0882` n `161`; fx avg `0.0014` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.7182` n `1262`
- 1h: commodity avg `-0.0206` n `13`; crypto_alt avg `-1.017` n `239`; crypto_major avg `-0.91` n `8`; equity avg `-1.2143` n `161`; fx avg `0.0327` n `6`; index avg `-0.1172` n `27`; metal avg `0.0067` n `20`; unknown avg `5.5902` n `1248`
- 4h: commodity avg `-0.1935` n `13`; crypto_alt avg `-1.3732` n `239`; crypto_major avg `-1.1876` n `8`; equity avg `-2.0055` n `161`; fx avg `-0.0029` n `6`; index avg `-0.2047` n `27`; metal avg `-0.0811` n `20`; unknown avg `5.2382` n `1204`
- 24h: commodity avg `0.2095` n `13`; crypto_alt avg `-1.0554` n `239`; crypto_major avg `-0.1041` n `8`; equity avg `3.3421` n `161`; fx avg `-0.1622` n `6`; index avg `0.3387` n `27`; metal avg `-0.0734` n `20`; unknown avg `3.9108` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
