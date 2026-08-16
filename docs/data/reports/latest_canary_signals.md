# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T11:31:00.523701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0154` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `0.0019` n `114`; fx avg `-0.0111` n `6`; index avg `0.0026` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0411` n `791`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.02` n `230`; crypto_major avg `0.0281` n `8`; equity avg `-0.0364` n `114`; fx avg `-0.0056` n `6`; index avg `0.0052` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0821` n `791`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `0.0799` n `230`; crypto_major avg `-0.0449` n `8`; equity avg `-0.0368` n `114`; fx avg `-0.0112` n `6`; index avg `-0.0092` n `25`; metal avg `0.0136` n `20`; unknown avg `0.0437` n `791`
- 24h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0693` n `230`; crypto_major avg `0.1474` n `8`; equity avg `0.3392` n `114`; fx avg `-0.009` n `6`; index avg `0.0533` n `25`; metal avg `0.0254` n `20`; unknown avg `0.0758` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
