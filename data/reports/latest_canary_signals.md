# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T09:52:25.527749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1978` n `228`; crypto_major avg `0.0578` n `8`; equity avg `-0.0197` n `78`; fx avg `0.0` n `6`; index avg `0.0018` n `23`; metal avg `0.005` n `18`; unknown avg `-0.1472` n `702`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.4856` n `228`; crypto_major avg `0.4947` n `8`; equity avg `0.0311` n `78`; fx avg `-0.0007` n `6`; index avg `0.0064` n `23`; metal avg `0.0247` n `18`; unknown avg `-0.0205` n `702`
- 4h: commodity avg `-0.0878` n `12`; crypto_alt avg `0.8467` n `228`; crypto_major avg `0.021` n `8`; equity avg `0.0447` n `78`; fx avg `-0.0067` n `6`; index avg `0.0101` n `23`; metal avg `0.0324` n `18`; unknown avg `-0.1813` n `662`
- 24h: commodity avg `0.0493` n `12`; crypto_alt avg `1.2167` n `228`; crypto_major avg `-0.0233` n `8`; equity avg `0.325` n `78`; fx avg `0.0382` n `6`; index avg `0.0192` n `23`; metal avg `-0.0105` n `18`; unknown avg `0.1542` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
