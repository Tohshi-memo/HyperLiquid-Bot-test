# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T05:07:33.348268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0787` n `13`; crypto_alt avg `-0.1861` n `239`; crypto_major avg `-0.099` n `8`; equity avg `-0.1967` n `163`; fx avg `-0.0048` n `6`; index avg `-0.0255` n `27`; metal avg `-0.0213` n `20`; unknown avg `0.227` n `1258`
- 1h: commodity avg `-0.1615` n `13`; crypto_alt avg `-0.4878` n `239`; crypto_major avg `-0.113` n `8`; equity avg `-0.2217` n `163`; fx avg `-0.0095` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0269` n `20`; unknown avg `7.7564` n `1260`
- 4h: commodity avg `-0.3323` n `13`; crypto_alt avg `-0.8279` n `239`; crypto_major avg `-0.4986` n `8`; equity avg `-1.3245` n `163`; fx avg `-0.012` n `6`; index avg `-0.1144` n `27`; metal avg `-0.4518` n `20`; unknown avg `9.8323` n `1252`
- 24h: commodity avg `0.0955` n `13`; crypto_alt avg `-0.6977` n `239`; crypto_major avg `-0.2309` n `8`; equity avg `-0.4076` n `163`; fx avg `-0.0872` n `6`; index avg `-0.0392` n `27`; metal avg `-0.8834` n `20`; unknown avg `257.7792` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
