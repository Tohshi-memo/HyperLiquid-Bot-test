# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T21:07:20.248596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0839` n `12`; crypto_alt avg `0.1458` n `228`; crypto_major avg `0.1895` n `8`; equity avg `0.007` n `67`; fx avg `0.0137` n `6`; index avg `-0.0233` n `23`; metal avg `-0.1126` n `18`; unknown avg `-0.0302` n `396`
- 1h: commodity avg `0.2937` n `12`; crypto_alt avg `-0.1465` n `228`; crypto_major avg `-0.0679` n `8`; equity avg `0.003` n `67`; fx avg `0.0178` n `6`; index avg `-0.0731` n `23`; metal avg `-0.2041` n `18`; unknown avg `-0.2774` n `396`
- 4h: commodity avg `0.2968` n `12`; crypto_alt avg `-0.5261` n `228`; crypto_major avg `-0.4128` n `8`; equity avg `0.0869` n `67`; fx avg `0.0581` n `6`; index avg `-0.0208` n `23`; metal avg `-0.3385` n `18`; unknown avg `-0.6085` n `396`
- 24h: commodity avg `1.2984` n `12`; crypto_alt avg `-2.5356` n `228`; crypto_major avg `-0.4381` n `8`; equity avg `0.5775` n `67`; fx avg `0.1145` n `6`; index avg `-0.0209` n `23`; metal avg `-0.507` n `18`; unknown avg `-0.0067` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
