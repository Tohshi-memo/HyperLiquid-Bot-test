# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T22:37:39.038248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `0.2678` n `239`; crypto_major avg `0.2207` n `8`; equity avg `0.731` n `163`; fx avg `0.0069` n `6`; index avg `0.0906` n `27`; metal avg `0.0001` n `20`; unknown avg `11.0452` n `1265`
- 1h: commodity avg `0.0487` n `13`; crypto_alt avg `0.0238` n `239`; crypto_major avg `0.0163` n `8`; equity avg `0.4333` n `163`; fx avg `0.0111` n `6`; index avg `0.0617` n `27`; metal avg `-0.0301` n `20`; unknown avg `2.6108` n `1257`
- 4h: commodity avg `-0.1956` n `13`; crypto_alt avg `1.2542` n `239`; crypto_major avg `1.1252` n `8`; equity avg `2.1017` n `163`; fx avg `-0.0178` n `6`; index avg `0.2135` n `27`; metal avg `-0.075` n `20`; unknown avg `2.5156` n `1233`
- 24h: commodity avg `0.2312` n `13`; crypto_alt avg `0.4199` n `239`; crypto_major avg `0.1732` n `8`; equity avg `0.6929` n `163`; fx avg `0.0166` n `6`; index avg `0.064` n `27`; metal avg `-0.0111` n `20`; unknown avg `6.3183` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
