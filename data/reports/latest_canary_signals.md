# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T22:07:43.364707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `13`; crypto_alt avg `0.3113` n `239`; crypto_major avg `0.2393` n `8`; equity avg `0.1371` n `158`; fx avg `-0.0176` n `6`; index avg `-0.0291` n `27`; metal avg `-0.0053` n `20`; unknown avg `-1.0652` n `1258`
- 1h: commodity avg `-0.0976` n `13`; crypto_alt avg `0.4427` n `239`; crypto_major avg `0.0904` n `8`; equity avg `0.5472` n `158`; fx avg `-0.0213` n `6`; index avg `0.0135` n `27`; metal avg `-0.0449` n `20`; unknown avg `-1.0741` n `1258`
- 4h: commodity avg `-0.0661` n `13`; crypto_alt avg `-0.2634` n `239`; crypto_major avg `-0.6037` n `8`; equity avg `-0.0122` n `158`; fx avg `-0.0093` n `6`; index avg `-0.0492` n `27`; metal avg `-0.0645` n `20`; unknown avg `-0.8128` n `1194`
- 24h: commodity avg `-1.8848` n `13`; crypto_alt avg `1.6185` n `239`; crypto_major avg `1.722` n `8`; equity avg `-1.2942` n `158`; fx avg `0.0581` n `6`; index avg `0.0479` n `27`; metal avg `1.2121` n `20`; unknown avg `-0.4856` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.266`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
