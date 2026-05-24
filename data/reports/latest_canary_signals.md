# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T07:07:16.482335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0867` n `12`; crypto_alt avg `-0.0423` n `228`; crypto_major avg `-0.0266` n `8`; equity avg `0.0273` n `67`; fx avg `-0.0085` n `6`; index avg `0.0366` n `23`; metal avg `0.0163` n `18`; unknown avg `-0.033` n `396`
- 1h: commodity avg `0.0694` n `12`; crypto_alt avg `0.2727` n `228`; crypto_major avg `0.3058` n `8`; equity avg `-0.028` n `67`; fx avg `0.0` n `6`; index avg `0.0135` n `23`; metal avg `-0.0545` n `18`; unknown avg `-0.3491` n `396`
- 4h: commodity avg `-0.3186` n `12`; crypto_alt avg `-0.2912` n `228`; crypto_major avg `0.325` n `8`; equity avg `0.0903` n `67`; fx avg `0.0102` n `6`; index avg `0.0218` n `23`; metal avg `0.0947` n `18`; unknown avg `-0.0719` n `386`
- 24h: commodity avg `-2.9388` n `12`; crypto_alt avg `2.4782` n `228`; crypto_major avg `3.3523` n `8`; equity avg `2.4067` n `67`; fx avg `0.0281` n `6`; index avg `1.323` n `23`; metal avg `1.1981` n `18`; unknown avg `1.913` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
