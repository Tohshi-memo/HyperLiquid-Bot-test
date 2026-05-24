# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T17:22:16.190750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0349` n `12`; crypto_alt avg `-0.057` n `228`; crypto_major avg `-0.1094` n `8`; equity avg `-0.0246` n `67`; fx avg `0.0066` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0658` n `18`; unknown avg `-0.1419` n `396`
- 1h: commodity avg `0.303` n `12`; crypto_alt avg `-0.0672` n `228`; crypto_major avg `-0.1702` n `8`; equity avg `0.0565` n `67`; fx avg `0.0051` n `6`; index avg `-0.0238` n `23`; metal avg `-0.1164` n `18`; unknown avg `-0.1516` n `396`
- 4h: commodity avg `0.6915` n `12`; crypto_alt avg `-0.4863` n `228`; crypto_major avg `-0.8039` n `8`; equity avg `-0.3728` n `67`; fx avg `0.0218` n `6`; index avg `-0.3327` n `23`; metal avg `-0.4144` n `18`; unknown avg `-0.2118` n `396`
- 24h: commodity avg `-1.2418` n `12`; crypto_alt avg `0.3988` n `228`; crypto_major avg `2.2515` n `8`; equity avg `1.6922` n `67`; fx avg `0.0911` n `6`; index avg `0.5521` n `23`; metal avg `0.5406` n `18`; unknown avg `1.0377` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
