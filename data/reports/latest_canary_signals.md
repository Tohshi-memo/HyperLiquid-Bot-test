# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T19:37:20.011658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1292` n `12`; crypto_alt avg `0.1572` n `228`; crypto_major avg `0.1589` n `8`; equity avg `0.0808` n `67`; fx avg `-0.0012` n `6`; index avg `0.0076` n `23`; metal avg `0.0193` n `18`; unknown avg `-0.1451` n `418`
- 1h: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.2117` n `228`; crypto_major avg `-0.2151` n `8`; equity avg `-0.1646` n `67`; fx avg `0.0037` n `6`; index avg `-0.0236` n `23`; metal avg `0.3053` n `18`; unknown avg `0.0546` n `418`
- 4h: commodity avg `-0.5864` n `12`; crypto_alt avg `-1.2688` n `228`; crypto_major avg `-1.0052` n `8`; equity avg `-0.0116` n `67`; fx avg `0.0515` n `6`; index avg `0.2721` n `23`; metal avg `0.345` n `18`; unknown avg `0.7555` n `418`
- 24h: commodity avg `0.7918` n `12`; crypto_alt avg `-2.2631` n `228`; crypto_major avg `-1.5811` n `8`; equity avg `-0.445` n `67`; fx avg `-0.1154` n `6`; index avg `0.4507` n `23`; metal avg `-1.0088` n `18`; unknown avg `0.1254` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
