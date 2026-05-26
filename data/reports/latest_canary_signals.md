# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T19:52:22.764962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0077` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `0.2639` n `228`; crypto_major avg `0.2089` n `8`; equity avg `0.0566` n `67`; fx avg `0.0041` n `6`; index avg `0.1015` n `23`; metal avg `0.1052` n `18`; unknown avg `-0.0592` n `418`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `0.1673` n `228`; crypto_major avg `-0.0045` n `8`; equity avg `-0.027` n `67`; fx avg `0.0169` n `6`; index avg `0.0717` n `23`; metal avg `0.314` n `18`; unknown avg `-0.1722` n `418`
- 4h: commodity avg `-0.4226` n `12`; crypto_alt avg `-0.9198` n `228`; crypto_major avg `-0.6331` n `8`; equity avg `0.1876` n `67`; fx avg `0.0448` n `6`; index avg `0.3746` n `23`; metal avg `0.3957` n `18`; unknown avg `0.3902` n `418`
- 24h: commodity avg `0.8236` n `12`; crypto_alt avg `-2.1205` n `228`; crypto_major avg `-1.436` n `8`; equity avg `-0.4595` n `67`; fx avg `-0.1151` n `6`; index avg `0.3947` n `23`; metal avg `-0.9249` n `18`; unknown avg `0.1854` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
