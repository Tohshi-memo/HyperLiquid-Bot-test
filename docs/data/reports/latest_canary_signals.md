# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T10:22:25.670123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0569` n `229`; crypto_major avg `0.1154` n `8`; equity avg `0.0039` n `88`; fx avg `-0.0077` n `6`; index avg `0.0009` n `25`; metal avg `0.0204` n `20`; unknown avg `0.058` n `763`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.7237` n `228`; crypto_major avg `1.0148` n `8`; equity avg `0.0107` n `88`; fx avg `-0.0222` n `6`; index avg `-0.0297` n `25`; metal avg `0.0255` n `20`; unknown avg `-0.0232` n `763`
- 4h: commodity avg `-0.097` n `12`; crypto_alt avg `1.0266` n `228`; crypto_major avg `1.1256` n `8`; equity avg `0.0894` n `88`; fx avg `-0.0926` n `6`; index avg `-0.0385` n `25`; metal avg `-0.0448` n `20`; unknown avg `1.0019` n `763`
- 24h: commodity avg `-0.435` n `12`; crypto_alt avg `2.7994` n `228`; crypto_major avg `3.0409` n `8`; equity avg `-2.0077` n `88`; fx avg `-0.1268` n `6`; index avg `-0.5748` n `25`; metal avg `1.1735` n `20`; unknown avg `3.5937` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
