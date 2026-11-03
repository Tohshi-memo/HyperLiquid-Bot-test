# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T04:52:27.276526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0579` n `13`; crypto_alt avg `-0.0893` n `239`; crypto_major avg `-0.0848` n `8`; equity avg `-0.0726` n `157`; fx avg `0.0019` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0065` n `20`; unknown avg `0.0665` n `1260`
- 1h: commodity avg `0.1039` n `13`; crypto_alt avg `0.3889` n `239`; crypto_major avg `0.2043` n `8`; equity avg `-0.3026` n `157`; fx avg `0.0006` n `6`; index avg `-0.051` n `27`; metal avg `-0.061` n `20`; unknown avg `0.1739` n `1196`
- 4h: commodity avg `0.188` n `13`; crypto_alt avg `-0.2768` n `239`; crypto_major avg `-0.2037` n `8`; equity avg `-0.3363` n `157`; fx avg `-0.0366` n `6`; index avg `-0.0507` n `27`; metal avg `-0.4236` n `20`; unknown avg `0.1076` n `1196`
- 24h: commodity avg `-0.8164` n `13`; crypto_alt avg `-3.0036` n `238`; crypto_major avg `-1.9769` n `8`; equity avg `-4.4231` n `157`; fx avg `-0.018` n `6`; index avg `-0.3628` n `27`; metal avg `-0.17` n `20`; unknown avg `7.8431` n `962`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
