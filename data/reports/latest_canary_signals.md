# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T11:07:24.486300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `13`; crypto_alt avg `-0.0434` n `239`; crypto_major avg `-0.1737` n `8`; equity avg `-0.0105` n `164`; fx avg `0.0025` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0431` n `20`; unknown avg `0.1254` n `1260`
- 1h: commodity avg `-0.0623` n `13`; crypto_alt avg `-0.1991` n `239`; crypto_major avg `-0.2566` n `8`; equity avg `0.2073` n `164`; fx avg `0.0375` n `6`; index avg `0.0067` n `27`; metal avg `-0.0762` n `20`; unknown avg `3.7265` n `1264`
- 4h: commodity avg `0.0177` n `13`; crypto_alt avg `-0.0563` n `239`; crypto_major avg `-0.289` n `8`; equity avg `0.499` n `164`; fx avg `0.1133` n `6`; index avg `0.1333` n `27`; metal avg `-0.1209` n `20`; unknown avg `260.9064` n `1222`
- 24h: commodity avg `0.1023` n `13`; crypto_alt avg `0.2867` n `239`; crypto_major avg `-0.1728` n `8`; equity avg `0.6831` n `164`; fx avg `0.0714` n `6`; index avg `0.2639` n `27`; metal avg `-0.1747` n `20`; unknown avg `1.5387` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
