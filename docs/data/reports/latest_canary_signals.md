# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T20:52:22.328666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0557` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `0.5459` n `228`; crypto_major avg `0.4321` n `8`; equity avg `0.0745` n `69`; fx avg `-0.0052` n `6`; index avg `-0.0225` n `23`; metal avg `-0.0305` n `18`; unknown avg `0.4293` n `422`
- 1h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.263` n `228`; crypto_major avg `-0.151` n `8`; equity avg `0.2355` n `69`; fx avg `-0.0103` n `6`; index avg `0.0059` n `23`; metal avg `0.0364` n `18`; unknown avg `0.6561` n `422`
- 4h: commodity avg `0.0928` n `12`; crypto_alt avg `-0.4234` n `228`; crypto_major avg `-0.8911` n `8`; equity avg `0.0589` n `69`; fx avg `-0.017` n `6`; index avg `0.1646` n `23`; metal avg `-0.1521` n `18`; unknown avg `-0.4487` n `422`
- 24h: commodity avg `-0.1407` n `12`; crypto_alt avg `-3.6011` n `228`; crypto_major avg `-4.6518` n `8`; equity avg `1.0358` n `69`; fx avg `0.0752` n `6`; index avg `0.663` n `23`; metal avg `0.4708` n `18`; unknown avg `-0.2207` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
