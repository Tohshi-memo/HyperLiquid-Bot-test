# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T17:52:25.770772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0155` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0437` n `13`; crypto_alt avg `0.0279` n `239`; crypto_major avg `0.2189` n `8`; equity avg `-0.2345` n `163`; fx avg `-0.007` n `6`; index avg `-0.0246` n `27`; metal avg `-0.0459` n `20`; unknown avg `-0.0453` n `1265`
- 1h: commodity avg `0.0353` n `13`; crypto_alt avg `0.3094` n `239`; crypto_major avg `0.702` n `8`; equity avg `0.7914` n `163`; fx avg `0.0051` n `6`; index avg `0.1012` n `27`; metal avg `0.0595` n `20`; unknown avg `1.8775` n `1259`
- 4h: commodity avg `0.0459` n `13`; crypto_alt avg `-1.3237` n `239`; crypto_major avg `-1.1714` n `8`; equity avg `-1.7505` n `163`; fx avg `0.0622` n `6`; index avg `-0.1559` n `27`; metal avg `0.0175` n `20`; unknown avg `67.9942` n `1245`
- 24h: commodity avg `0.0536` n `13`; crypto_alt avg `-0.4597` n `239`; crypto_major avg `-0.142` n `8`; equity avg `-2.2538` n `163`; fx avg `0.0275` n `6`; index avg `-0.2694` n `27`; metal avg `-0.0184` n `20`; unknown avg `8.2166` n `1096`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
