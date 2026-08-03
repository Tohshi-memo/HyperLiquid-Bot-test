# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T10:07:35.259444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `0.1011` n `8`; equity avg `-0.0696` n `102`; fx avg `-0.0145` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0107` n `784`
- 1h: commodity avg `-0.0932` n `12`; crypto_alt avg `0.2632` n `230`; crypto_major avg `0.381` n `8`; equity avg `-0.3965` n `102`; fx avg `-0.0177` n `6`; index avg `-0.0469` n `25`; metal avg `-0.0669` n `20`; unknown avg `0.0914` n `784`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.1099` n `230`; crypto_major avg `-0.0728` n `8`; equity avg `-0.9677` n `102`; fx avg `0.0593` n `6`; index avg `-0.1021` n `25`; metal avg `-0.1322` n `20`; unknown avg `0.0439` n `784`
- 24h: commodity avg `-0.1927` n `12`; crypto_alt avg `-0.8578` n `230`; crypto_major avg `-0.2665` n `8`; equity avg `-0.343` n `102`; fx avg `-0.1858` n `6`; index avg `-0.125` n `25`; metal avg `-0.1451` n `20`; unknown avg `1.0381` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
