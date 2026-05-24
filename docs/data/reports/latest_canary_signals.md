# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T13:07:14.774875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0927` n `228`; crypto_major avg `0.1507` n `8`; equity avg `0.0412` n `67`; fx avg `0.02` n `6`; index avg `-0.0526` n `23`; metal avg `-0.0341` n `18`; unknown avg `0.1747` n `396`
- 1h: commodity avg `0.0793` n `12`; crypto_alt avg `-0.1223` n `228`; crypto_major avg `0.1999` n `8`; equity avg `0.1281` n `67`; fx avg `0.0226` n `6`; index avg `-0.0766` n `23`; metal avg `-0.1299` n `18`; unknown avg `0.1681` n `396`
- 4h: commodity avg `0.1355` n `12`; crypto_alt avg `-0.4616` n `228`; crypto_major avg `0.3093` n `8`; equity avg `0.285` n `67`; fx avg `0.0103` n `6`; index avg `-0.1123` n `23`; metal avg `-0.1653` n `18`; unknown avg `-0.3709` n `396`
- 24h: commodity avg `-2.6876` n `12`; crypto_alt avg `2.7631` n `228`; crypto_major avg `4.3874` n `8`; equity avg `2.7196` n `67`; fx avg `0.0731` n `6`; index avg `1.0976` n `23`; metal avg `1.1684` n `18`; unknown avg `1.932` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
