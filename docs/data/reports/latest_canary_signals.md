# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T17:07:34.428290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `13`; crypto_alt avg `-0.0638` n `239`; crypto_major avg `-0.0976` n `8`; equity avg `0.0295` n `156`; fx avg `0.0106` n `6`; index avg `0.0043` n `27`; metal avg `-0.0005` n `20`; unknown avg `-0.1495` n `1257`
- 1h: commodity avg `-0.2998` n `13`; crypto_alt avg `-0.2701` n `239`; crypto_major avg `-0.1875` n `8`; equity avg `-0.4662` n `156`; fx avg `0.025` n `6`; index avg `-0.0284` n `27`; metal avg `0.0404` n `20`; unknown avg `-0.3886` n `1257`
- 4h: commodity avg `-0.7512` n `13`; crypto_alt avg `-0.3049` n `238`; crypto_major avg `-0.2826` n `8`; equity avg `-1.1183` n `156`; fx avg `0.0068` n `6`; index avg `0.0158` n `27`; metal avg `0.4293` n `20`; unknown avg `19.2082` n `1251`
- 24h: commodity avg `-1.1928` n `13`; crypto_alt avg `-2.2233` n `238`; crypto_major avg `-0.9472` n `8`; equity avg `-0.8625` n `156`; fx avg `0.2883` n `6`; index avg `0.2154` n `27`; metal avg `0.4104` n `20`; unknown avg `7.0806` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
