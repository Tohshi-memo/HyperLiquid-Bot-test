# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T22:52:25.777147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `13`; crypto_alt avg `-0.028` n `235`; crypto_major avg `-0.0431` n `8`; equity avg `-0.0777` n `150`; fx avg `-0.0003` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0031` n `20`; unknown avg `-0.1219` n `1077`
- 1h: commodity avg `-0.0728` n `13`; crypto_alt avg `0.1186` n `235`; crypto_major avg `0.073` n `8`; equity avg `0.1074` n `150`; fx avg `-0.0021` n `6`; index avg `0.0282` n `26`; metal avg `0.0449` n `20`; unknown avg `0.0137` n `1075`
- 4h: commodity avg `-0.1343` n `13`; crypto_alt avg `1.4657` n `235`; crypto_major avg `1.0973` n `8`; equity avg `0.5299` n `150`; fx avg `0.0189` n `6`; index avg `0.0831` n `26`; metal avg `0.0753` n `20`; unknown avg `0.0478` n `1007`
- 24h: commodity avg `0.4669` n `13`; crypto_alt avg `-2.8028` n `235`; crypto_major avg `-3.2667` n `8`; equity avg `-2.6567` n `150`; fx avg `0.0579` n `6`; index avg `-0.3484` n `26`; metal avg `0.0523` n `20`; unknown avg `6.3046` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
