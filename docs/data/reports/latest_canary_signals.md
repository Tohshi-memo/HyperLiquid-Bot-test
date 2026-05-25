# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T15:37:20.036671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `0.0637` n `228`; crypto_major avg `0.0646` n `8`; equity avg `-0.0094` n `67`; fx avg `0.0061` n `6`; index avg `-0.0344` n `23`; metal avg `-0.132` n `18`; unknown avg `1.0057` n `405`
- 1h: commodity avg `-0.3099` n `12`; crypto_alt avg `0.0595` n `228`; crypto_major avg `-0.1322` n `8`; equity avg `0.0573` n `67`; fx avg `0.0074` n `6`; index avg `0.0048` n `23`; metal avg `-0.0446` n `18`; unknown avg `0.8565` n `405`
- 4h: commodity avg `0.0545` n `12`; crypto_alt avg `0.4587` n `228`; crypto_major avg `0.1039` n `8`; equity avg `0.0613` n `67`; fx avg `-0.021` n `6`; index avg `0.0474` n `23`; metal avg `0.1446` n `18`; unknown avg `0.7605` n `397`
- 24h: commodity avg `-0.7459` n `12`; crypto_alt avg `2.1296` n `228`; crypto_major avg `0.8207` n `8`; equity avg `1.0156` n `67`; fx avg `0.0055` n `6`; index avg `0.4917` n `23`; metal avg `1.4527` n `18`; unknown avg `0.9536` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
