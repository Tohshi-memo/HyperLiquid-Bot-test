# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T08:22:23.284485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.0729` n `239`; crypto_major avg `0.0124` n `8`; equity avg `0.1344` n `164`; fx avg `0.007` n `6`; index avg `0.0209` n `27`; metal avg `0.0075` n `20`; unknown avg `68.9614` n `1262`
- 1h: commodity avg `-0.0808` n `13`; crypto_alt avg `0.0034` n `239`; crypto_major avg `-0.006` n `8`; equity avg `-0.0159` n `164`; fx avg `0.0389` n `6`; index avg `0.0179` n `27`; metal avg `-0.0777` n `20`; unknown avg `72.9046` n `1222`
- 4h: commodity avg `-0.0505` n `13`; crypto_alt avg `0.0354` n `239`; crypto_major avg `0.5031` n `8`; equity avg `0.8111` n `164`; fx avg `0.0579` n `6`; index avg `0.1294` n `27`; metal avg `0.0406` n `20`; unknown avg `33.6955` n `1200`
- 24h: commodity avg `0.1488` n `13`; crypto_alt avg `0.1644` n `239`; crypto_major avg `-0.6657` n `8`; equity avg `0.2284` n `164`; fx avg `0.0499` n `6`; index avg `0.1747` n `27`; metal avg `-0.1367` n `20`; unknown avg `3.6673` n `1103`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
