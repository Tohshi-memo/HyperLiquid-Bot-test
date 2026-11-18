# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T01:37:38.508407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0672` n `13`; crypto_alt avg `-0.0912` n `239`; crypto_major avg `-0.2443` n `8`; equity avg `-0.4331` n `163`; fx avg `-0.019` n `6`; index avg `-0.0573` n `27`; metal avg `0.0823` n `20`; unknown avg `-0.0101` n `1266`
- 1h: commodity avg `-0.1` n `13`; crypto_alt avg `-0.5448` n `239`; crypto_major avg `-0.7975` n `8`; equity avg `-1.0789` n `163`; fx avg `-0.0039` n `6`; index avg `-0.1578` n `27`; metal avg `0.0054` n `20`; unknown avg `2.4053` n `1264`
- 4h: commodity avg `-0.0605` n `13`; crypto_alt avg `-0.2461` n `239`; crypto_major avg `-0.0774` n `8`; equity avg `0.0438` n `163`; fx avg `-0.072` n `6`; index avg `-0.0526` n `27`; metal avg `-0.2134` n `20`; unknown avg `3.366` n `1211`
- 24h: commodity avg `0.2462` n `13`; crypto_alt avg `0.7921` n `239`; crypto_major avg `0.7568` n `8`; equity avg `0.209` n `163`; fx avg `-0.1037` n `6`; index avg `-0.0668` n `27`; metal avg `-0.2749` n `20`; unknown avg `7.0797` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
