# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T15:22:14.550901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4064` n `12`; crypto_alt avg `0.055` n `228`; crypto_major avg `0.094` n `8`; equity avg `0.0414` n `67`; fx avg `0.0021` n `6`; index avg `-0.053` n `23`; metal avg `0.1234` n `18`; unknown avg `0.0228` n `396`
- 1h: commodity avg `-0.3681` n `12`; crypto_alt avg `0.2254` n `228`; crypto_major avg `0.1184` n `8`; equity avg `0.0833` n `67`; fx avg `-0.0015` n `6`; index avg `-0.1459` n `23`; metal avg `0.1524` n `18`; unknown avg `0.1839` n `396`
- 4h: commodity avg `0.6116` n `12`; crypto_alt avg `-1.0697` n `228`; crypto_major avg `-0.851` n `8`; equity avg `-0.1853` n `67`; fx avg `0.0008` n `6`; index avg `-0.3201` n `23`; metal avg `-0.5054` n `18`; unknown avg `1.4737` n `396`
- 24h: commodity avg `-1.5873` n `12`; crypto_alt avg `0.5393` n `228`; crypto_major avg `2.1165` n `8`; equity avg `1.6598` n `67`; fx avg `0.0856` n `6`; index avg `0.505` n `23`; metal avg `0.5848` n `18`; unknown avg `1.9462` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
