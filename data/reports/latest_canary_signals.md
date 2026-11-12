# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T03:37:27.475536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `13`; crypto_alt avg `0.0638` n `239`; crypto_major avg `-0.0316` n `8`; equity avg `-0.2354` n `161`; fx avg `0.0109` n `6`; index avg `-0.037` n `27`; metal avg `0.0381` n `20`; unknown avg `0.0942` n `1260`
- 1h: commodity avg `-0.1006` n `13`; crypto_alt avg `-0.2528` n `239`; crypto_major avg `-0.329` n `8`; equity avg `-0.783` n `161`; fx avg `-0.0603` n `6`; index avg `-0.0856` n `27`; metal avg `0.0067` n `20`; unknown avg `18.7277` n `1254`
- 4h: commodity avg `-0.0636` n `13`; crypto_alt avg `0.0613` n `239`; crypto_major avg `-0.022` n `8`; equity avg `-0.2428` n `161`; fx avg `-0.1101` n `6`; index avg `-0.0502` n `27`; metal avg `0.0661` n `20`; unknown avg `21.1073` n `1248`
- 24h: commodity avg `0.0808` n `13`; crypto_alt avg `-1.7439` n `239`; crypto_major avg `-0.5825` n `8`; equity avg `0.7095` n `161`; fx avg `-0.2083` n `6`; index avg `0.0593` n `27`; metal avg `-0.389` n `20`; unknown avg `2.4881` n `1139`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
