# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T12:52:38.597693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-0.0235` n `237`; crypto_major avg `-0.0914` n `8`; equity avg `-0.0676` n `151`; fx avg `0.0182` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0508` n `20`; unknown avg `-0.005` n `1193`
- 1h: commodity avg `-0.0358` n `13`; crypto_alt avg `0.5672` n `237`; crypto_major avg `0.3507` n `8`; equity avg `0.1882` n `151`; fx avg `0.0085` n `6`; index avg `0.0246` n `26`; metal avg `-0.0969` n `20`; unknown avg `0.1645` n `1171`
- 4h: commodity avg `0.2009` n `13`; crypto_alt avg `-0.2857` n `237`; crypto_major avg `-0.2196` n `8`; equity avg `0.4832` n `151`; fx avg `0.0191` n `6`; index avg `0.0237` n `26`; metal avg `-0.044` n `20`; unknown avg `0.4272` n `1169`
- 24h: commodity avg `-0.1945` n `13`; crypto_alt avg `-0.0694` n `237`; crypto_major avg `0.7331` n `8`; equity avg `2.8606` n `151`; fx avg `-0.0284` n `6`; index avg `0.4693` n `26`; metal avg `0.1381` n `20`; unknown avg `1.1582` n `969`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2004`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1536`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1323`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0582`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
