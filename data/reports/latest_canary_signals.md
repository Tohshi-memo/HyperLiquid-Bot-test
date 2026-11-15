# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T17:07:27.955408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3359` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `0.1026` n `239`; crypto_major avg `0.1685` n `8`; equity avg `-0.0116` n `162`; fx avg `-0.0062` n `6`; index avg `-0.0126` n `27`; metal avg `0.0181` n `20`; unknown avg `0.1269` n `1259`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.1439` n `239`; crypto_major avg `-0.0484` n `8`; equity avg `0.2247` n `162`; fx avg `-0.0004` n `6`; index avg `0.0027` n `27`; metal avg `0.0128` n `20`; unknown avg `22.8796` n `1263`
- 4h: commodity avg `-0.0829` n `13`; crypto_alt avg `-1.4162` n `239`; crypto_major avg `-1.3129` n `8`; equity avg `0.0428` n `162`; fx avg `-0.0053` n `6`; index avg `0.023` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.9062` n `1256`
- 24h: commodity avg `0.0662` n `13`; crypto_alt avg `-0.8296` n `239`; crypto_major avg `0.0185` n `8`; equity avg `0.4604` n `162`; fx avg `-0.0162` n `6`; index avg `0.0585` n `27`; metal avg `-0.106` n `20`; unknown avg `0.5798` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
