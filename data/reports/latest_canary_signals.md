# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T06:52:26.678254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0504` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0931` n `12`; crypto_alt avg `-0.8127` n `228`; crypto_major avg `-0.7264` n `8`; equity avg `-0.2875` n `74`; fx avg `-0.0107` n `6`; index avg `-0.0361` n `23`; metal avg `0.0019` n `18`; unknown avg `0.8987` n `425`
- 1h: commodity avg `-0.2444` n `12`; crypto_alt avg `0.0848` n `228`; crypto_major avg `-0.0586` n `8`; equity avg `-0.029` n `74`; fx avg `-0.0074` n `6`; index avg `0.1027` n `23`; metal avg `0.1117` n `18`; unknown avg `1.219` n `415`
- 4h: commodity avg `-0.5397` n `12`; crypto_alt avg `-1.7416` n `228`; crypto_major avg `-1.0783` n `8`; equity avg `0.1316` n `74`; fx avg `-0.0186` n `6`; index avg `-0.0279` n `23`; metal avg `-0.129` n `18`; unknown avg `-0.5706` n `415`
- 24h: commodity avg `-1.5556` n `12`; crypto_alt avg `-3.3088` n `228`; crypto_major avg `-2.4275` n `8`; equity avg `-6.1549` n `74`; fx avg `-0.1825` n `6`; index avg `-4.0408` n `23`; metal avg `-4.1916` n `18`; unknown avg `1.3979` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
