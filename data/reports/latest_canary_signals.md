# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T15:20:40.130528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4297` n `12`; crypto_alt avg `0.0469` n `228`; crypto_major avg `0.0833` n `8`; equity avg `0.0248` n `67`; fx avg `0.0021` n `6`; index avg `-0.0493` n `23`; metal avg `0.1305` n `18`; unknown avg `0.0445` n `396`
- 1h: commodity avg `-0.3914` n `12`; crypto_alt avg `0.2172` n `228`; crypto_major avg `0.1076` n `8`; equity avg `0.0668` n `67`; fx avg `-0.0015` n `6`; index avg `-0.1423` n `23`; metal avg `0.1595` n `18`; unknown avg `0.1986` n `396`
- 4h: commodity avg `0.5876` n `12`; crypto_alt avg `-1.0775` n `228`; crypto_major avg `-0.8617` n `8`; equity avg `-0.2027` n `67`; fx avg `0.0008` n `6`; index avg `-0.3165` n `23`; metal avg `-0.4984` n `18`; unknown avg `1.4814` n `396`
- 24h: commodity avg `-1.6097` n `12`; crypto_alt avg `0.5324` n `228`; crypto_major avg `2.105` n `8`; equity avg `1.6431` n `67`; fx avg `0.0856` n `6`; index avg `0.5086` n `23`; metal avg `0.5918` n `18`; unknown avg `1.976` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
