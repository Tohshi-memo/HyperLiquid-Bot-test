# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T00:16:05.035034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0727` n `12`; crypto_alt avg `-0.0837` n `228`; crypto_major avg `0.0249` n `8`; equity avg `-0.0604` n `67`; fx avg `0.0094` n `6`; index avg `0.0003` n `23`; metal avg `0.0033` n `18`; unknown avg `-0.1002` n `396`
- 1h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.0504` n `228`; crypto_major avg `0.0798` n `8`; equity avg `-0.0182` n `67`; fx avg `-0.0056` n `6`; index avg `0.1083` n `23`; metal avg `0.1207` n `18`; unknown avg `0.2457` n `396`
- 4h: commodity avg `-0.9761` n `12`; crypto_alt avg `0.5491` n `228`; crypto_major avg `0.6383` n `8`; equity avg `0.6924` n `67`; fx avg `0.0837` n `6`; index avg `0.3262` n `23`; metal avg `0.6133` n `18`; unknown avg `0.266` n `396`
- 24h: commodity avg `-2.957` n `12`; crypto_alt avg `2.6845` n `228`; crypto_major avg `2.3135` n `8`; equity avg `1.9637` n `67`; fx avg `0.0574` n `6`; index avg `0.9971` n `23`; metal avg `0.9532` n `18`; unknown avg `0.9828` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
